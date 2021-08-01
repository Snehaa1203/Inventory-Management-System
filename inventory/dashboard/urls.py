from django.urls import path
from .views import *
urlpatterns = [
	path('dashboard/',index,name='index'),
	path('staff/',staff,name='staff'),
	path('staff/detail/<int:pk>',staff_detail,name='staff_detail'),
	path('product/',product,name='product'),
	path('product/delete/<int:pk>',product_delete,name='product_delete'),
	path('product/update/<int:pk>',product_update,name='product_update'),
	path('order/',order,name='order')
]
