import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .managers import UserManager


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        BUYER = "buyer", "Buyer"
        SELLER = "seller", "Seller"
        ADMIN = "admin", "Admin"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=150, blank=True, default="")
    last_name = models.CharField(max_length=150, blank=True, default="")
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.BUYER)
    avatar_url = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        indexes = [models.Index(fields=["email"], name="idx_users_email")]

    def __str__(self):
        return self.email


class SellerProfile(TimeStampedModel):
    class ApprovalStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller_profile")
    store_name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    headline = models.CharField(max_length=180, blank=True, default="")
    description = models.TextField(blank=True, default="")
    website_url = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, default="")
    approval_status = models.CharField(
        max_length=20,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.PENDING,
    )
    total_sales = models.PositiveIntegerField(default=0)
    rating_avg = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    class Meta:
        db_table = "seller_profiles"
        indexes = [models.Index(fields=["slug"], name="idx_seller_profiles_slug")]

    def __str__(self):
        return self.store_name


class Category(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField(blank=True, default="")
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="children",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "categories"
        indexes = [models.Index(fields=["slug"], name="idx_categories_slug")]

    def __str__(self):
        return self.name


class Listing(TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        PAUSED = "paused", "Paused"
        ARCHIVED = "archived", "Archived"

    class ProductType(models.TextChoices):
        DIGITAL = "digital", "Digital"
        SERVICE = "service", "Service"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, related_name="listings")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="listings")
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    product_type = models.CharField(
        max_length=20,
        choices=ProductType.choices,
        default=ProductType.DIGITAL,
    )
    delivery_days = models.PositiveIntegerField(default=0)
    revision_count = models.PositiveIntegerField(default=0)
    tags = models.JSONField(default=list, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    sales_count = models.PositiveIntegerField(default=0)
    rating_avg = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    class Meta:
        db_table = "listings"
        indexes = [
            models.Index(fields=["seller"], name="idx_listings_seller_id"),
            models.Index(fields=["category"], name="idx_listings_category_id"),
            models.Index(fields=["status"], name="idx_listings_status"),
        ]

    def __str__(self):
        return self.title


class ListingImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="images")
    image_url = models.TextField()
    alt_text = models.CharField(max_length=180, blank=True, default="")
    sort_order = models.PositiveIntegerField(default=0)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "listing_images"
        ordering = ["sort_order", "created_at"]
        indexes = [models.Index(fields=["listing"], name="idx_listing_images_listing_id")]

    def __str__(self):
        return f"{self.listing} image"


class DigitalFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="digital_files")
    file_url = models.TextField()
    file_name = models.CharField(max_length=255)
    file_size_bytes = models.PositiveBigIntegerField(default=0)
    mime_type = models.CharField(max_length=120, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "digital_files"
        indexes = [models.Index(fields=["listing"], name="idx_digital_files_listing_id")]

    def __str__(self):
        return self.file_name


class Cart(TimeStampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        CHECKED_OUT = "checked_out", "Checked out"
        ABANDONED = "abandoned", "Abandoned"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = "carts"

    def __str__(self):
        return f"{self.user.email} cart"


class CartItem(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        db_table = "cart_items"
        constraints = [
            models.UniqueConstraint(fields=["cart", "listing"], name="unique_cart_listing")
        ]
        indexes = [models.Index(fields=["cart"], name="idx_cart_items_cart_id")]

    def __str__(self):
        return f"{self.quantity} x {self.listing}"


class Order(TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        FULFILLED = "fulfilled", "Fulfilled"
        CANCELLED = "cancelled", "Cancelled"
        REFUNDED = "refunded", "Refunded"

    class PaymentStatus(models.TextChoices):
        SIMULATED = "simulated", "Simulated"
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        FAILED = "failed", "Failed"
        REFUNDED = "refunded", "Refunded"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.SIMULATED,
    )
    payment_reference = models.CharField(max_length=120, blank=True, default="")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    platform_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        db_table = "orders"
        indexes = [models.Index(fields=["buyer"], name="idx_orders_buyer_id")]

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    class FulfillmentStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        DELIVERED = "delivered", "Delivered"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT, related_name="order_items")
    seller = models.ForeignKey(SellerProfile, on_delete=models.PROTECT, related_name="order_items")
    title_snapshot = models.CharField(max_length=180)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    fulfillment_status = models.CharField(
        max_length=20,
        choices=FulfillmentStatus.choices,
        default=FulfillmentStatus.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_items"
        indexes = [models.Index(fields=["order"], name="idx_order_items_order_id")]

    def __str__(self):
        return self.title_snapshot


class Review(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.SET_NULL,
        related_name="reviews",
        blank=True,
        null=True,
    )
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=160, blank=True, default="")
    body = models.TextField(blank=True, default="")

    class Meta:
        db_table = "reviews"
        constraints = [
            models.UniqueConstraint(fields=["listing", "buyer"], name="unique_listing_buyer_review")
        ]
        indexes = [models.Index(fields=["listing"], name="idx_reviews_listing_id")]

    def __str__(self):
        return f"{self.rating} stars for {self.listing}"


class Favorite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "favorites"
        constraints = [
            models.UniqueConstraint(fields=["user", "listing"], name="unique_user_listing_favorite")
        ]
        indexes = [models.Index(fields=["user"], name="idx_favorites_user_id")]

    def __str__(self):
        return f"{self.user.email} favorited {self.listing}"


class Conversation(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer_conversations")
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, related_name="conversations")
    listing = models.ForeignKey(
        Listing,
        on_delete=models.SET_NULL,
        related_name="conversations",
        blank=True,
        null=True,
    )
    subject = models.CharField(max_length=180, blank=True, default="")

    class Meta:
        db_table = "conversations"
        constraints = [
            models.UniqueConstraint(
                fields=["buyer", "seller", "listing"],
                name="unique_buyer_seller_listing_conversation",
            )
        ]
        indexes = [models.Index(fields=["buyer"], name="idx_conversations_buyer_id")]

    def __str__(self):
        return self.subject or f"Conversation {self.id}"


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"
        ordering = ["created_at"]
        indexes = [models.Index(fields=["conversation"], name="idx_messages_conversation_id")]

    def __str__(self):
        return f"Message {self.id}"


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=180)
    body = models.TextField(blank=True, default="")
    data = models.JSONField(default=dict, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notifications"
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["user"], name="idx_notifications_user_id")]

    def __str__(self):
        return self.title
