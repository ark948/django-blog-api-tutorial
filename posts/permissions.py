from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users can only see list view
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # read permissions are allowed GET, HEAD, or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions are only allowed to the author of views
        return obj.author == request.user