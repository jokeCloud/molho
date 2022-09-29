from django.urls import path

from . import views

app_name = 'molho_app'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>', views.product_list,
         name='product_list_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
]