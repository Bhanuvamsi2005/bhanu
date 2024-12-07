from django.db import models

# Create your models here.
from django.db import models
class Task(models.Model):
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    def _str_(self):
         return self.title

class StudentList(models.Model):
    Register_Number=models.CharField(max_length=20,unique=True)
    Name=models.CharField(max_length=100)

    def _str_(self):
        return self.Register_Number

from django.db import models

class Rating(models.Model):
    username = models.CharField(max_length=100)
    quality_of_service = models.IntegerField()
    website_interface = models.IntegerField()
    overall_experience = models.IntegerField()

    def __str__(self):
        return f"{self.username}'s Rating"

from django.db import models

class Order(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    phone = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"


from django.db import models

class Order2(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    total_cost = models.IntegerField()
    def __str__(self):
        return f"{self.product} - {self.quantity}"
