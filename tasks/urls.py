from django.urls import path

from tasks.views import (
    CreateTaskView,
)


urlpatterns = [
    path("create/", CreateTaskView.as_view(), name="create_task"),
]
