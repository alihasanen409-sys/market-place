from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

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
    User,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = ("email", "role", "is_active", "is_staff", "date_joined")
    list_filter = ("role", "is_active", "is_staff", "is_superuser")
    search_fields = ("email", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Profile", {"fields": ("first_name", "last_name", "role", "avatar_url", "bio")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Dates", {"fields": ("last_login", "date_joined", "updated_at")}),
    )
    readonly_fields = ("last_login", "date_joined", "updated_at")
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "role", "is_staff", "is_superuser"),
            },
        ),
    )


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ("store_name", "user", "approval_status", "rating_avg", "total_sales")
    list_filter = ("approval_status",)
    search_fields = ("store_name", "headline", "user__email")
    prepopulated_fields = {"slug": ("store_name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 0


class DigitalFileInline(admin.TabularInline):
    model = DigitalFile
    extra = 0


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "seller", "category", "price", "status", "product_type", "rating_avg")
    list_filter = ("status", "product_type", "category")
    search_fields = ("title", "description", "seller__store_name")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ListingImageInline, DigitalFileInline]


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Notification)
