from rest_framework.routers import DefaultRouter

from .views import (
    CartItemViewSet,
    CartViewSet,
    CategoryViewSet,
    ConversationViewSet,
    DigitalFileViewSet,
    FavoriteViewSet,
    ListingImageViewSet,
    ListingViewSet,
    MessageViewSet,
    NotificationViewSet,
    OrderItemViewSet,
    OrderViewSet,
    ReviewViewSet,
    SellerProfileViewSet,
    UserViewSet,
)


router = DefaultRouter()
router.register("users", UserViewSet)
router.register("seller-profiles", SellerProfileViewSet)
router.register("categories", CategoryViewSet)
router.register("listings", ListingViewSet)
router.register("listing-images", ListingImageViewSet)
router.register("digital-files", DigitalFileViewSet)
router.register("carts", CartViewSet)
router.register("cart-items", CartItemViewSet)
router.register("orders", OrderViewSet)
router.register("order-items", OrderItemViewSet)
router.register("reviews", ReviewViewSet)
router.register("favorites", FavoriteViewSet)
router.register("conversations", ConversationViewSet)
router.register("messages", MessageViewSet)
router.register("notifications", NotificationViewSet)

urlpatterns = router.urls
