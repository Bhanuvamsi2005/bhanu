from django import forms
from .models import Blog

class TaskForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title']

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']