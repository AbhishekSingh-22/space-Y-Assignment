from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description='This project mainly has 4 tables - Products, Employees, Customers, Orders for tracking all the things required by a small scale shopping mall.\nThe API endpoints are:\n1. baseurl/api/v1/products/\n2. baseurl/api/v1/product/id\n3. baseurl/api/v1/employees/\n4. baseurl/api/v1/employee/id\n5. baseurl/api/v1/customers/\n6. baseurl/api/v1/customer/id/\n7. baseurl/api/v1/orders/\n8. baseurl/api/v1/order/id\n9. baseurl/api/v1/place-order/\n\n\nNOTE: For accessing the above APIs, you first need to get and access token for it and pass it in the request authorization section as the bearer token.\n   Without it you will be unauthorized to access it.\n  To get the access token and refresh token visit:- baseurl/api/v1/register/ if you are a new user, and if you already an user with you account created then visit:- baseurl/api/token/ to get the access token and refresh token.\n\nRequest structure for placing order:-\n    {\n"customer_id": ,\n"employee_id": ,\n"products":[\n{"product_id": , "quantity": },\n{"product_id": , "quantity": }\n]\n}',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include('billing.urls')),
]
