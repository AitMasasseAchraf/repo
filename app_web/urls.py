
from django.urls import path
from . import views

urlpatterns = [
    path('Brand_form/', views.Brand_form, name='brand_insert'),
    path('Brands/' , views.Brand_list,name='brand_list'),
    path('<int:id>/', views.Brand_form, name='brand_update'),
    path('delete/<int:id>/', views.Brand_delete,name='Brand_delete')
    

]