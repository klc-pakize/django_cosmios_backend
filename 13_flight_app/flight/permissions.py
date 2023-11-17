from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        return bool(request.user.is_staff)