from decimal import Decimal

import cloudinary
import cloudinary.uploader
from django.conf import settings
from django.db import transaction
from django.utils.text import slugify
from rest_framework import serializers

from .models import Cart, DigitalFile, ListingImage, Notification, Order, OrderItem


def validate_upload(file_obj, allowed_content_types, max_bytes):
    content_type = getattr(file_obj, "content_type", "")
    if content_type not in allowed_content_types:
        raise serializers.ValidationError({"file": "This file type is not allowed."})
    if file_obj.size > max_bytes:
        raise serializers.ValidationError({"file": "This file is too large."})


def upload_to_cloudinary(file_obj, folder, resource_type="auto"):
    if not all(settings.CLOUDINARY.values()):
        raise serializers.ValidationError(
            {"cloudinary": "Cloudinary credentials are not configured."}
        )

    cloudinary.config(**settings.CLOUDINARY, secure=True)
    result = cloudinary.uploader.upload(
        file_obj,
        folder=folder,
        resource_type=resource_type,
        use_filename=True,
        unique_filename=True,
    )
    return result["secure_url"]


def create_listing_image_from_upload(listing, file_obj, alt_text="", is_primary=False):
    validate_upload(
        file_obj,
        settings.ALLOWED_IMAGE_CONTENT_TYPES,
        settings.MAX_IMAGE_UPLOAD_BYTES,
    )
    image_url = upload_to_cloudinary(file_obj, "marketplace/listing-images", "image")
    return ListingImage.objects.create(
        listing=listing,
        image_url=image_url,
        alt_text=alt_text,
        is_primary=is_primary,
    )


def create_digital_file_from_upload(listing, file_obj):
    validate_upload(
        file_obj,
        settings.ALLOWED_DIGITAL_FILE_CONTENT_TYPES,
        settings.MAX_DIGITAL_FILE_UPLOAD_BYTES,
    )
    file_url = upload_to_cloudinary(file_obj, "marketplace/digital-files", "auto")
    return DigitalFile.objects.create(
        listing=listing,
        file_url=file_url,
        file_name=file_obj.name,
        file_size_bytes=file_obj.size,
        mime_type=getattr(file_obj, "content_type", ""),
    )


@transaction.atomic
def checkout_cart(user):
    cart = Cart.objects.select_for_update().prefetch_related("items__listing__seller").get(
        user=user,
        status=Cart.Status.ACTIVE,
    )
    items = list(cart.items.all())
    if not items:
        raise serializers.ValidationError({"cart": "The cart is empty."})

    subtotal = sum((item.unit_price * item.quantity for item in items), Decimal("0.00"))
    platform_fee = (subtotal * Decimal("0.05")).quantize(Decimal("0.01"))
    total = subtotal + platform_fee
    order = Order.objects.create(
        buyer=user,
        status=Order.Status.PAID,
        payment_status=Order.PaymentStatus.SIMULATED,
        payment_reference=f"SIM-{slugify(str(cart.id))[:24]}",
        subtotal=subtotal,
        platform_fee=platform_fee,
        total=total,
    )

    for item in items:
        listing = item.listing
        OrderItem.objects.create(
            order=order,
            listing=listing,
            seller=listing.seller,
            title_snapshot=listing.title,
            unit_price=item.unit_price,
            quantity=item.quantity,
            total_price=item.unit_price * item.quantity,
            fulfillment_status=OrderItem.FulfillmentStatus.DELIVERED,
        )
        listing.sales_count += item.quantity
        listing.save(update_fields=["sales_count", "updated_at"])
        Notification.objects.create(
            user=listing.seller.user,
            type="sale",
            title="New simulated sale",
            body=f"{user.email} bought {listing.title}.",
            data={"order_id": str(order.id), "listing_id": str(listing.id)},
        )

    cart.status = Cart.Status.CHECKED_OUT
    cart.save(update_fields=["status", "updated_at"])
    cart.items.all().delete()
    Notification.objects.create(
        user=user,
        type="order",
        title="Order confirmed",
        body="Your simulated checkout is complete.",
        data={"order_id": str(order.id)},
    )
    return order
