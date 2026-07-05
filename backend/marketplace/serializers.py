from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import (
    Cart,
    CartItem,
    Category,
    Conversation,
    DigitalFile,
    Favorite,
    Listing,
    ListingImage,
    Message,
    Notification,
    Order,
    OrderItem,
    Review,
    SellerProfile,
)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "role",
            "avatar_url",
            "bio",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
            "updated_at",
        ]
        read_only_fields = ["id", "last_login", "date_joined", "updated_at"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = [
            "id",
            "user",
            "store_name",
            "slug",
            "headline",
            "description",
            "website_url",
            "location",
            "approval_status",
            "total_sales",
            "rating_avg",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "parent",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ["id", "listing", "image_url", "alt_text", "sort_order", "is_primary", "created_at"]
        read_only_fields = ["id", "created_at"]


class DigitalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalFile
        fields = ["id", "listing", "file_url", "file_name", "file_size_bytes", "mime_type", "created_at"]
        read_only_fields = ["id", "created_at"]


class ListingSerializer(serializers.ModelSerializer):
    images = ListingImageSerializer(many=True, read_only=True)
    digital_files = DigitalFileSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = [
            "id",
            "seller",
            "category",
            "title",
            "slug",
            "description",
            "short_description",
            "price",
            "status",
            "product_type",
            "delivery_days",
            "revision_count",
            "tags",
            "view_count",
            "sales_count",
            "rating_avg",
            "images",
            "digital_files",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "view_count", "sales_count", "rating_avg", "created_at", "updated_at"]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "cart", "listing", "quantity", "unit_price", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "status", "items", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "listing",
            "seller",
            "title_snapshot",
            "unit_price",
            "quantity",
            "total_price",
            "fulfillment_status",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "buyer",
            "status",
            "payment_status",
            "payment_reference",
            "subtotal",
            "platform_fee",
            "total",
            "items",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "listing",
            "buyer",
            "order_item",
            "rating",
            "title",
            "body",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ["id", "user", "listing", "created_at"]
        read_only_fields = ["id", "created_at"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "conversation", "sender", "body", "is_read", "created_at"]
        read_only_fields = ["id", "created_at"]


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            "id",
            "buyer",
            "seller",
            "listing",
            "subject",
            "messages",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "user", "type", "title", "body", "data", "is_read", "created_at"]
        read_only_fields = ["id", "created_at"]
