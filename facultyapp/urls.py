from django.urls import path,include
from . import views
app_name='facultyapp'
urlpatterns=[
    path('facultyhomepage/', views.facultyhomepage, name='facultyhomepage'),
    path('addblog/',views.addblog,name='addblog'),
    path('<int:pk>/delete/',views.deleteblog,name='deleteblog'),
    path('add-product/', views.add_product, name='add_product'),
]