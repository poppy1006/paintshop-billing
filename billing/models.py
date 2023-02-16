from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=255)
    quantity=models.IntegerField(max_length=5)
    category=models.CharField(max_length=255)
    price=models.FloatField(max_length=10)

class Bill(models.Model):
    invoice_number=models.CharField(max_length=30)
    item_name=models.TextField(max_length=5000)
    total_amount=models.FloatField(max_length=10)
    date_of_purchase=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=255)
    phone_number=models.IntegerField(max_length=15)
    sales_man=models.CharField(max_length=255)
    credit_or_not=models.CharField(max_length=50,default="Payed")

class Sales_man(models.Model):
    name=models.CharField(max_length=255)
    phone_number=models.IntegerField(max_length=15)
    
class Category(models.Model):
    name=models.CharField(max_length=255)

class Invoice(models.Model):
    number=models.IntegerField()
    
    





