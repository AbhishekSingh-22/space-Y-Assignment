from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'employee', 'placed_at', 'status', 'total_price']


# class OrderSerializer(serializers.ModelSerializer):
#     customer = PrimaryKeyRelatedField(queryset=Customer.objects.all())
#     employee = PrimaryKeyRelatedField(queryset=Employee.objects.all())
#     # order_items = OrderItemSerializer(many=True)
#     class Meta:
#         model = Order
#         fields = ('id', 'customer', 'employee', 'status', 'total_price')

class OrderPlacementSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    employee_id = serializers.IntegerField()
    products = serializers.ListField(child=serializers.DictField())

    def create(self, validated_data):
        customer_id = validated_data['customer_id']
        employee_id = validated_data['employee_id']
        products_data = validated_data['products']
        
        # Retrieve customer and employee objects
        customer = get_object_or_404(Customer, pk=customer_id)
        employee = get_object_or_404(Employee, pk=employee_id)
        
        # Initialize total price
        total_price = 0
        
        # Loop through the products data to calculate total price and update product quantities
        for product_data in products_data:
            product_id = product_data['product_id']
            quantity = product_data['quantity']

            
            # Retrieve product object
            product = get_object_or_404(Product, pk=product_id)
            
            if quantity > product.available_qty:
                raise serializers.ValidationError({"error": f"Insufficient available quantity for {product.name}"})

            # Calculate subtotal for this product
            subtotal = product.price * quantity
            
            # Update product quantities
            product.available_qty -= quantity
            product.qty_sold += quantity
            product.save()
            
            # Add subtotal to total price
            total_price += subtotal
        
        employee.number_of_orders_processed +=1
        employee.total_sales += total_price
        employee.save()

        # Create the order
        order = Order.objects.create(customer=customer, employee=employee, total_price=total_price)
        return order
