from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsAuthenticatedOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True

        user = getattr(obj, "user", None) or getattr(obj, "buyer", None) or getattr(obj, "sender", None)
        return bool(user == request.user)


class IsAdminOrOwnerUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and (request.user.is_staff or obj == request.user))


class IsSellerOrAdminForWrite(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user
            and request.user.is_authenticated
            and (request.user.is_staff or request.user.role == "seller")
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user
            and (
                request.user.is_staff
                or getattr(getattr(obj, "seller", None), "user", None) == request.user
            )
        )


class IsBuyerOrAdminForWrite(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user
            and request.user.is_authenticated
            and (request.user.is_staff or request.user.role == "buyer")
        )
