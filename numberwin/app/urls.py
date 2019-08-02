from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('ang/',views.ang,name='ang'),
    path('add/',views.add,name='add')
]
