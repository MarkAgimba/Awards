# from rest_framework.authorization import SAFE_METHODS, BasePermission

# class IsAdminOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         else:
#             return request.user.is_staff