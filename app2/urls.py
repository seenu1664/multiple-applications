app_name='nothing'
from django.urls import path
from app2.views import *

urlpatterns = [
    path('one/',one,name='one'),
    path('two/',two,name='two'),
    
]
