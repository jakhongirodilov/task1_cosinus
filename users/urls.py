from django.urls import path
from .views import SignUpView, logout_view
from .views import profile_view, update_profile

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", logout_view, name="logout"),
    path("profile/<int:id>/", profile_view, name="profile"),
    path('profile/update/', update_profile, name="profile_update")
]