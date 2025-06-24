# api/permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of an object or admins to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow if user is admin/staff
        if request.user.is_staff:
            return True

        # Only allow access if the user is the creator of the object
        return obj.created_by == request.user
