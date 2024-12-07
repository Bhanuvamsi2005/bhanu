from django.urls import path,include
from . import views
app_name='studentapp'
urlpatterns = [
    path('studenthomepage/',views.studenthomepage,name='studenthomepage'),
    path('buyproductspagecall/',views.buyproductspagecall,name='buyproductspagecall'),
    path('buyproductspagelogic/', views.buyproductspagelogic, name='buyproductspagelogic'),
    path('fertilizerpagecall/',views.fertilizerpagecall,name='fertilizerpagecall'),
    path('fertilizerpagelogic/',views.fertilizerpagelogic,name='fertilizerpagelogic'),

]