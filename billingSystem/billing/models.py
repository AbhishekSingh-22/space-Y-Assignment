from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    available_qty = models.IntegerField(default=0)
    qty_sold = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    employee_id = models.CharField(max_length=20)
    job_title = models.CharField(max_length=100)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    number_of_orders_processed = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    products = models.ManyToManyField('Product')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order ID: {self.order_id}, Date: {self.order_date}, Total Price: {self.total_price}"
