# # myapp/middleware.py
# from django.contrib.auth import logout
# from django.http import HttpResponseRedirect
# from django.urls import reverse
#
# class AdminLoginRequiredMiddleware:
#     """
#     Forces a user to log in again when accessing the admin page.
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         # Check if the request path starts with '/admin/' (for the admin page)
#         if request.path.startswith('/admin/') and request.user.is_authenticated:
#             # Prevent logout if already on the login page or logging in
#
#                  # Force log out the user
#             return HttpResponseRedirect(('admin:login'))  # Redirect to login page
#         return self.get_response(request)
