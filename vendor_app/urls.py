from django.urls import path
from .views import *

urlpatterns =[
   path('vendor_register',vendor_register,name='vendor_register'),  
   path('vendor_login', vendor_login, name='vendor_login'),
   path('vendor_dashboard', vendor_dashboard, name='vendor_dashboard'),



]