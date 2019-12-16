Django multiple permissions
===========================

[![Python](https://img.shields.io/pypi/pyversions/multiple-permissions)](https://img.shields.io/pypi/pyversions/multiple-permissions)
[![License](https://img.shields.io/github/license/aram2726/django_multiple_permissions)](https://img.shields.io/github/license/aram2726/django_multiple_permissions)

Usage
------

* install package

```shell script
$ pip install multiple-permissions
```

* add apps.core to installed apps

```python
INSTALLED_APPS = [
    ...,
    "multiple_permissions",
    ...,
]
```

* add apps.core.middlewares to MIDDLEWARE list

```python
MIDDLEWARE = [
    ...,
    "multiple_permissions.middlewares.PermissionMiddleware",
]
```

* Add "permission_classes" attribute to view classes

```python
from django.views.generic import ListView, CreateView

from multiple_permissions.permissions import IsAuthenticated, IsSuperuser, IsManager


class PollsListView(ListView):
    permission_classes = (IsAuthenticated,)
    ...


class PollsCreateView(CreateView):
    permission_classes = (IsSuperuser, IsManager)
    ...
```

#### Creating new permissions

* create new file in your apps named `permissions.py` and write the followng code

* **note that your user should have `is_manager` attribute or model field otherwise you'll catch AttributeError**

```python
from multiple_permissions.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view=None):
        if request.user.is_authenticated and request.user.is_active and request.user.is_manager:
            return True
        return False

```
