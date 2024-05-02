from django.urls import path
from . import views

app_name = 'hw_4app'

urlpatterns = [

    path('', views.index, name='index'),
    path('client/<int:client_id>/', views.client_order, name='client_order'),

]