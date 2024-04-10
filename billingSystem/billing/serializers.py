from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'available_qty', 'qty_sold', 'price']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone_number', 'employee_id', 'job_title', 'total_sales', 'number_of_orders_processed']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'mobile_number']


# class OrderItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer()  # Nested serializer for product details

#     class Meta:
#         model = OrderItem
#         fields = '__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     customer = CustomerSerializer()
#     employee = EmployeeSerializer()
#     order_items = OrderItemSerializer(many=True)  # Nested serializer for order items

#     class Meta:
#         model = Order
#         fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'price')

class OrderSerializer(serializers.ModelSerializer):
    customer = PrimaryKeyRelatedField(queryset=Customer.objects.all())
    employee = PrimaryKeyRelatedField(queryset=Employee.objects.all())
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ('id', 'customer', 'employee', 'status', 'order_items')
