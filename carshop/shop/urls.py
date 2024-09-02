from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:transport_id>', views.single_transport, name='single_transport')
]
