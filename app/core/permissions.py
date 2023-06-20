from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class IsStaff(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user.is_staff


class IsAuthorOrReadOnly(IsStaff):
    def has_object_permission(self, request, view, obj):
        return (
            super().has_object_permission(request, view, obj)
            or request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class NewsAuthorCanDeleteComment(IsAuthorOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' and obj.news.author == request.user:
            return True
        return super().has_object_permission(request, view, obj)
