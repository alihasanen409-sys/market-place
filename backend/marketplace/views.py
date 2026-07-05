from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import decorators, permissions, response, status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser

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
from .serializers import (
    CartItemSerializer,
    CartSerializer,
    CategorySerializer,
    ConversationSerializer,
    DigitalFileSerializer,
    FavoriteSerializer,
    ListingImageSerializer,
    ListingSerializer,
    MessageSerializer,
    NotificationSerializer,
    OrderItemSerializer,
    OrderSerializer,
    ReviewSerializer,
    SellerProfileSerializer,
    UserSerializer,
)
from .services import (
    checkout_cart,
    create_digital_file_from_upload,
    create_listing_image_from_upload,
)


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    search_fields = ["email", "first_name", "last_name"]
    ordering_fields = ["date_joined", "email", "role"]

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class SellerProfileViewSet(viewsets.ModelViewSet):
    queryset = SellerProfile.objects.select_related("user").all().order_by("-created_at")
    serializer_class = SellerProfileSerializer
    search_fields = ["store_name", "headline", "description", "location"]
    filterset_fields = ["approval_status", "location"]
    ordering_fields = ["created_at", "rating_avg", "total_sales"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related("parent").all().order_by("name")
    serializer_class = CategorySerializer
    search_fields = ["name", "description"]
    filterset_fields = ["is_active", "parent"]
    ordering_fields = ["name", "created_at"]


class ListingViewSet(viewsets.ModelViewSet):
    queryset = (
        Listing.objects.select_related("seller", "category")
        .prefetch_related("images", "digital_files")
        .all()
        .order_by("-created_at")
    )
    serializer_class = ListingSerializer
    search_fields = ["title", "description", "short_description"]
    filterset_fields = ["seller", "category", "status", "product_type"]
    ordering_fields = ["created_at", "price", "rating_avg", "sales_count", "view_count"]

    @decorators.action(
        detail=True,
        methods=["post"],
        parser_classes=[MultiPartParser, FormParser],
        permission_classes=[permissions.IsAuthenticated],
    )
    def upload_image(self, request, pk=None):
        listing = self.get_object()
        file_obj = request.FILES.get("file")
        if not file_obj:
            return response.Response({"file": "This field is required."}, status=status.HTTP_400_BAD_REQUEST)
        image = create_listing_image_from_upload(
            listing,
            file_obj,
            alt_text=request.data.get("alt_text", ""),
            is_primary=request.data.get("is_primary") in ["true", "True", True],
        )
        return response.Response(ListingImageSerializer(image).data, status=status.HTTP_201_CREATED)

    @decorators.action(
        detail=True,
        methods=["post"],
        parser_classes=[MultiPartParser, FormParser],
        permission_classes=[permissions.IsAuthenticated],
    )
    def upload_file(self, request, pk=None):
        listing = self.get_object()
        file_obj = request.FILES.get("file")
        if not file_obj:
            return response.Response({"file": "This field is required."}, status=status.HTTP_400_BAD_REQUEST)
        digital_file = create_digital_file_from_upload(listing, file_obj)
        return response.Response(DigitalFileSerializer(digital_file).data, status=status.HTTP_201_CREATED)


class ListingImageViewSet(viewsets.ModelViewSet):
    queryset = ListingImage.objects.select_related("listing").all().order_by("sort_order")
    serializer_class = ListingImageSerializer
    filterset_fields = ["listing", "is_primary"]
    ordering_fields = ["sort_order", "created_at"]


class DigitalFileViewSet(viewsets.ModelViewSet):
    queryset = DigitalFile.objects.select_related("listing").all().order_by("-created_at")
    serializer_class = DigitalFileSerializer
    filterset_fields = ["listing", "mime_type"]
    search_fields = ["file_name", "mime_type"]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.select_related("user").prefetch_related("items").all().order_by("-created_at")
    serializer_class = CartSerializer
    filterset_fields = ["user", "status"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)

    @decorators.action(detail=False, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def checkout(self, request):
        order = checkout_cart(request.user)
        return response.Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.select_related("cart", "listing").all().order_by("-created_at")
    serializer_class = CartItemSerializer
    filterset_fields = ["cart", "listing"]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related("buyer").prefetch_related("items").all().order_by("-created_at")
    serializer_class = OrderSerializer
    filterset_fields = ["buyer", "status", "payment_status"]
    ordering_fields = ["created_at", "subtotal", "total"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(buyer=self.request.user)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.select_related("order", "listing", "seller").all().order_by("-created_at")
    serializer_class = OrderItemSerializer
    filterset_fields = ["order", "listing", "seller", "fulfillment_status"]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related("listing", "buyer", "order_item").all().order_by("-created_at")
    serializer_class = ReviewSerializer
    filterset_fields = ["listing", "buyer", "rating"]
    ordering_fields = ["created_at", "rating"]


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.select_related("user", "listing").all().order_by("-created_at")
    serializer_class = FavoriteSerializer
    filterset_fields = ["user", "listing"]


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = (
        Conversation.objects.select_related("buyer", "seller", "listing")
        .prefetch_related("messages")
        .all()
        .order_by("-updated_at")
    )
    serializer_class = ConversationSerializer
    filterset_fields = ["buyer", "seller", "listing"]
    search_fields = ["subject"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(Q(buyer=self.request.user) | Q(seller__user=self.request.user))


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related("conversation", "sender").all().order_by("created_at")
    serializer_class = MessageSerializer
    filterset_fields = ["conversation", "sender", "is_read"]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.select_related("user").all().order_by("-created_at")
    serializer_class = NotificationSerializer
    filterset_fields = ["user", "type", "is_read"]
    search_fields = ["title", "body"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)

    @decorators.action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def mark_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save(update_fields=["is_read"])
        return response.Response(NotificationSerializer(notification).data)

    @decorators.action(detail=False, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def mark_all_read(self, request):
        self.get_queryset().update(is_read=True)
        return response.Response({"status": "ok"})
