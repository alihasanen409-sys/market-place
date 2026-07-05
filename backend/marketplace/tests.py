import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import serializers
from rest_framework.test import APIClient

from .models import Cart, CartItem, Category, Listing, SellerProfile
from .services import checkout_cart, validate_upload


pytestmark = pytest.mark.django_db


def create_listing():
    User = get_user_model()
    seller_user = User.objects.create_user(email="seller@example.com", password="password123", role="seller")
    seller = SellerProfile.objects.create(user=seller_user, store_name="Studio", slug="studio")
    category = Category.objects.create(name="Design", slug="design")
    return Listing.objects.create(
        seller=seller,
        category=category,
        title="Brand Kit",
        slug="brand-kit",
        description="Complete brand kit",
        price="20.00",
        status=Listing.Status.PUBLISHED,
    )


def test_user_can_register_and_get_jwt_tokens():
    client = APIClient()
    response = client.post(
        "/api/users/",
        {"email": "buyer@example.com", "password": "password123", "role": "buyer"},
        format="json",
    )
    assert response.status_code == 201

    token_response = client.post(
        "/api/auth/token/",
        {"email": "buyer@example.com", "password": "password123"},
        format="json",
    )
    assert token_response.status_code == 200
    assert "access" in token_response.data
    assert "refresh" in token_response.data


def test_checkout_cart_creates_simulated_order():
    User = get_user_model()
    user = User.objects.create_user(email="buyer@example.com", password="password123")
    listing = create_listing()
    cart = Cart.objects.create(user=user)
    CartItem.objects.create(cart=cart, listing=listing, quantity=2, unit_price=listing.price)

    order = checkout_cart(user)

    assert order.items.count() == 1
    assert order.payment_status == "simulated"
    assert order.total > order.subtotal


def test_upload_validation_blocks_disallowed_content_type():
    upload = SimpleUploadedFile("bad.exe", b"data", content_type="application/x-msdownload")

    with pytest.raises(serializers.ValidationError):
      validate_upload(upload, {"image/png"}, 1024)
