from django.urls import path
from .views import (gestion_list, per_product_view, add_product, 
delete_gestion, update_gestion)

urlpatterns = [

    path('', gestion_list, name='gestion_list'),
    path('per_product/<int:pk>', per_product_view, name='per_product'),
    path('add_gestion/', add_product, name='add_gestion'),
    path('delete/<int:pk>', delete_gestion, name='delete_gestion'),
    path('update/<int:pk>', update_gestion, name='update_gestion'),

]