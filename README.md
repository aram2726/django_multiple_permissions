Django multiple permissions
===========================

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
