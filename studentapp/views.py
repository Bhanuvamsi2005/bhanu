from django.shortcuts import render


def studenthomepage(request):
    return render(request,'studentapp/studenthomepage.html')

def buyproductspagecall(request):
    return render(request,'studentapp/buyproducts.html')
def buyproductspagelogic(request):
    return render(request, 'studentapp/buyproducts.html')

def fertilizerpagecall(request):
    return render(request, 'studentapp/buyfertilizers.html')
def fertilizerpagelogic(request):
    return render(request, 'studentapp/buyfertilizers.html')

