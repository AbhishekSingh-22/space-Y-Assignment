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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="placed")  # Add order status field
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order: {self.id} - Customer: {self.customer}"

    def calculate_and_update_total(self):
        total = 0
        for item in self.orderitem_set.all():
            total += item.quantity * item.price
        self.total_price = total
        self.save()  # Update order with calculated total

    def update_product_quantities(self):
        for item in self.orderitem_set.all():
            product = item.product
            if product.available_qty >= item.quantity:
                product.available_qty -= item.quantity
                product.save()
            else:
                raise ValueError(f"Insufficient quantity for {product.name}")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Item: {self.id} - {self.product.name} (x{self.quantity})"


