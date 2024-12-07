from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']

from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentList
        fields=['Register_Number','Name']

from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['username', 'quality_of_service', 'website_interface', 'overall_experience']
        widgets = {
            'quality_of_service': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'website_interface': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'overall_experience': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
        }


from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'phone', 'address']


from django import forms
from .models import Order2

class Order2Form(forms.ModelForm):
    class Meta:
        model = Order2
        fields = ['product', 'quantity', 'phone', 'address' , 'total_cost']
