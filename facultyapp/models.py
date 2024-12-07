from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    def _str_(self):
         return self.title

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.name