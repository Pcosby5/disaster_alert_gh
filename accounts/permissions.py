from rest_framework import permissions

class IsNADMOAdmin(permissions.BasePermission):
    """
    Custom permission to allow only NADMO admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_admin



class CanSubmitReport(permissions.BasePermission):
    """
    Allow any user (authenticated or anonymous) to POST a disaster report.
    Restrict other actions to authenticated users only.
    """

    def has_permission(self, request, view):
        if view.action in ['create', 'list']:
            return True  # Allow any user to create or view reports
        return request.user and request.user.is_authenticated
