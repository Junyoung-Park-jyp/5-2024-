from django.urls import path
from .views import *


app_name = 'payments'
urlpatterns = [
    path('', pay),
    path('list', pay_list),
    path('settle', settle),
]
