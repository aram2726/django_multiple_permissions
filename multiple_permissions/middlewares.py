from django.core.exceptions import PermissionDenied


class PermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        if getattr(view_func, "view_class", None):
            if getattr(view_func.view_class, "multiple_permissions", None):
                # assign permission_classes attribute of view class to permission_classes variable
                permission_classes = view_func.view_class.multiple_permissions
                conditions = []
                # loop through permission_classes
                for permission_class in permission_classes:
                    # check if request user correspond to permission class conditions
                    conditions.append(permission_class().has_permission(request))
                # check if there is any matching condition
                if not any(conditions):
                    raise PermissionDenied
