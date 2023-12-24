from django.urls import path
from .views import index, create_product, product_view, edit_product, delete_product, my_products

urlpatterns = [
    path('', index, name="home"),
    path('new_product/', create_product, name="new_product"),
    path('product/<int:id>/', product_view, name="product"),
    path('product/edit/<int:id>/', edit_product, name="edit_product"),
    path('product/delete/<int:id>/', delete_product, name="delete_product"),
    path('my_products/', my_products, name="my_products")
]