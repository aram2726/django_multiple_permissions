from abc import ABCMeta, abstractmethod


class BasePermission(metaclass=ABCMeta):
    @abstractmethod
    def has_permission(self, request, view=None):
        pass


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view=None):
        if request.user.is_authenticated and request.user.is_active:
            return True
        return False


class IsSuperuser(BasePermission):
    def has_permission(self, request, view=None):
        if request.user.is_authenticated and request.user.is_active and request.user.is_superuser:
            return True
        return False
