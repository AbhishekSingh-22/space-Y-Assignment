from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Sum

# register class for authentication and getting access token and refresh token
class RegisterUser(APIView):
    """
    API endpoint for registering new users and getting access and refresh token for the same
    """
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status':403, 'errors': serializer.errors, 'message' : "Something went wrong!"})
        
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status':200,
        'payload': serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'message': "your data is saved"})


# product apis
class ProductListCreate(generics.ListCreateAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# customer apis
class CustomerListCreate(generics.ListCreateAPIView):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# employee apis
class EmployeeListCreate(generics.ListCreateAPIView):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    
# api for viewing all orders made till now
class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
        
# api for placing order
class OrderPlacementView(APIView):
    """
    API endpoint that allows employees to place order for customers.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = OrderPlacementSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            total_price = order.total_price
            return Response({'message': 'Order placed successfully.','total_price': total_price}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Analytics api
class AnalyticsAPIView(generics.ListAPIView):
    """
    API for getting the analysis of best employee and product sold the most
    """
    serializer_class = AnalyticsSerializer

    def get_queryset(self):
        # Retrieve employee with the most sales
        top_employee = Employee.objects.annotate(total_sales_amount=Sum('total_sales')).order_by('-total_sales_amount').first()
        employee_with_most_sales = top_employee.name if top_employee else None

        # Retrieve product that has been sold the most
        top_product = Product.objects.order_by('-qty_sold').first()
        product_most_sold = top_product.name if top_product else None

        # Retrieve top employees and products by sales
        top_employees = Employee.objects.annotate(total_sales_amount=Sum('total_sales')).order_by('-total_sales_amount')[:5]
        top_products = Product.objects.order_by('-qty_sold')[:5]

        return [{'employee_with_most_sales': employee_with_most_sales,
                 'product_most_sold': product_most_sold,
                 'top_employees': [employee.name for employee in top_employees],
                 'top_products': [product.name for product in top_products]}]







            
