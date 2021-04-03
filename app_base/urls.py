from django.urls import path

from .views import index, infor

urlpatterns = [
    path('', index, name='index'),
    path('infor/', infor, name='infor'),
]