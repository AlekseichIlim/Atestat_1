from rest_framework import permissions


class IsActivePermission(permissions.BasePermission):
    """Определяет, является ли пользователь активным"""

    def has_object_permission(self, request, view, obj):
        if request.user.is_active:
            return True
        return False
