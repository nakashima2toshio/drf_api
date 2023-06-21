from django.urls import path
from ec_app import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    path('customer_profiles/', views.CustomerProfileList.as_view(), name='customerprofile-list'),
    path('customer_profiles/<int:pk>/', views.CustomerProfileDetail.as_view(), name='customerprofile-detail'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('product_categories/', views.ProductCategoryList.as_view(), name='productcategory-list'),
    path('product_categories/<int:pk>/', views.ProductCategoryDetail.as_view(), name='productcategory-detail'),
]
