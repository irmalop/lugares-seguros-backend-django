from django.urls import path

from initial import views

urlpatterns = [
    path('', views.HelloDRF.as_view(), name='index')
]