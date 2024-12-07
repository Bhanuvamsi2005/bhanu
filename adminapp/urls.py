from django.urls import path,include
from . import views
#from .views import chatbot_response, chatbot_view

urlpatterns = [
    path('',views.projecthomepage, name='projecthomepage'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('loginpagecall/',views.loginpagecall,name='loginpagecall'),
    path('registerpagecall/',views.registerpagecall,name='registerpagecall'),
    path('registerpagecall/', views.registerpagecall, name='registerpagecall'),
    path('registerpagelogic/', views.registerpagelogic, name='registerpagelogic'),
    path('loginpagelogic/', views.loginpagelogic, name='loginpagelogic'),
    path('logout/',views.logout,name='logout'),
    path('add_student/',views.add_student,name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('teammatespagecall/',views.teammatespagecall,name='teammatespagecall'),
    path('teammatespagelogic/',views.teammatespagelogic,name='teammatespagelogic'),
    path('get_weather/', views.get_weather, name='get_weather'),
    #path('', chatbot_view, name='chatbot_view'),
    #path('chatbot/', chatbot_response, name='chatbot'),
    #path('ratingpagecall/',views.ratingpagecall,name='ratingpagecall'),
    #path('ratingpagelogic/',views.ratingpagelogic,name='ratingpagelogic'),
    path('rate_service/', views.rate_service, name='rate_service'),
    path('ratingthankyou/',views.ratingthankyou,name='ratingthankyou'),
    path('externalcsspagecall/',views.externalcsspagecall,name='externalcsspagecall'),
    path('externalpagelogic/',views.externalpagelogic,name='externalpagelogic'),
    path('uitrailpagecall/', views.uitrailpagecall, name='uitrailpagecall'),
    path('uitrailpagelogic/', views.uitrailpagelogic, name='uitrailpagelogic'),
    #path('assistant/', views.activate_assistant, name='activate_assistant'),
    #path('chat/', views.chatbot, name='chatbot'),
    path('assistant/', views.assistant, name='assistant'),
    path('assistantpagecall/', views.assistantpagecall, name='assistantpagecall'),
    path('order_confirmation', views.order_confirmation, name='order_confirmation'),
    path('order_success/', views.order_success, name='order_success'),
    path('cropsuggestions/', views.cropsuggestions, name='cropsuggestions'),

]