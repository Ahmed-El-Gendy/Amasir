from django.db import models


# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='phones')
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number


class BankAccount(models.Model):
    id = models.AutoField(primary_key=True)
    iban = models.CharField(max_length=34, unique=True)
    swift_code = models.CharField(max_length=11)
    account_name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bank_accounts')

    def __str__(self):
        return self.account_name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cart')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shopping Cart for {self.customer.name}"


class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
        ('delivered', 'Delivered'),
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='pending',
    )

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50)
    PAYMENT_CHOICES = [
        ('paid', 'Paid'),
        ('not_paid', 'Not Paid'),
    ]

    payment_status = models.CharField(
        max_length=50,
        choices=PAYMENT_CHOICES,
        default='not_paid',
    )

    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id}"


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()  # Assuming a rating out of 5
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer.name} for {self.product.name}"

