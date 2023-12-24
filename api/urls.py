from django.urls import path, include
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from .views import (
    ProductListAPIView,
    ProductDetailAPIView,
    ProductCreateAPIView,
    UserList,
    UserDetail
)

urlpatterns = [
    path('dj-rest-auth/', include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/account-confirm-email/<str:key>/", ConfirmEmailView.as_view(), name="account_confirm_email"),
    path("dj-rest-auth/registration/", RegisterView.as_view(serializer_class=CustomRegisterSerializer), name="custom_register"),

    path('products/', ProductListAPIView.as_view(), name='product-list-api'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create-api'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail-api'),

    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
]
