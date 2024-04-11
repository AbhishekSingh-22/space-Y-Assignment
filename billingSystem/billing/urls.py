from django.urls import path
from .views import *

urlpatterns = [
    # url for new registration of user
    path('register', RegisterUser.as_view()),

    # urls for product apis
    path('products', ProductListCreate.as_view(), name='product-list-create'),
    path('product/<int:pk>', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),

    # urls for customers api
    path('customers', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customer/<int:pk>', CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),

    # urls for employees api
    path('employees', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employee/<int:pk>', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),

    # urls for order apis
    path('place-order', OrderPlacementView.as_view(), name='place_order'),
    path('orders', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('order/<int:pk>', OrderDetailAPIView.as_view(), name='order-detail'),

    # url for analytics api
    path('analytics', AnalyticsAPIView.as_view(), name='analytics'),
] 