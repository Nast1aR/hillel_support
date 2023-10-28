from django.contrib import admin
from django.urls import path
from ...deprecated.exchange_rates import exchange_rates
from django.http import JsonResponse
from django.urls import path
from users.views import UserListView, UserCreateView, IssueCreateView, IssueListView

def signup(request):
    payload = {
        "id": 1,
        "username": "John",
        "full_name": "John Doe",
    }
    return JsonResponse(payload)

urlpatterns = [
    path('users/all/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('issues/create/', IssueCreateView.as_view(), name='issue-create'),
    path('issues/all/', IssueListView.as_view(), name='issue-list'),
    path("auth/", include("authentication.urls")),
    path("issues/", include("issues.urls"))
]
