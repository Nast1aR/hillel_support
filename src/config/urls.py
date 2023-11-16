from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def signup(request):
    payload = {
        "id": 1,
        "username": "John",
        "full_name": "John Doe",
    }
    return JsonResponse(payload)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
    path("issues/", include("issues.urls")),
]
