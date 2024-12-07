from django.shortcuts import render
def facultyhomepage(request):
    return render(request, 'facultyapp/facultyhomepage.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import TaskForm

def addblog(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:addblog')
    else:
        form = TaskForm()
    tasks = Blog.objects.all()
    return render(request, 'facultyapp/facultytasks.html', {'form': form, 'tasks': tasks})


def deleteblog(request, pk):
    task = get_object_or_404(Blog, pk=pk)
    task.delete()
    return redirect('facultyapp:addblog')


from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')  # Redirect to the same page after successful form submission
    else:
        form = ProductForm()

    # Fetch all products from the database to display them
    products = Product.objects.all()

    return render(request, 'add_product.html', {'form': form, 'products': products})