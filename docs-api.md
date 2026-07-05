# API Documentation

The backend exposes OpenAPI docs at:

```text
/api/docs/
```

JWT endpoints:

```text
POST /api/auth/token/
POST /api/auth/token/refresh/
```

Main CRUD resources:

```text
/api/users/
/api/seller-profiles/
/api/categories/
/api/listings/
/api/listing-images/
/api/digital-files/
/api/carts/
/api/cart-items/
/api/orders/
/api/order-items/
/api/reviews/
/api/favorites/
/api/conversations/
/api/messages/
/api/notifications/
```

Workflow endpoints:

```text
POST /api/listings/{id}/upload_image/
POST /api/listings/{id}/upload_file/
POST /api/carts/checkout/
POST /api/notifications/{id}/mark_read/
POST /api/notifications/mark_all_read/
```
