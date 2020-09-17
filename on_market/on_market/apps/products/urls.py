from django.urls import path, include
from . import views


app_name = 'products'
urlpatterns = [
	path('', views.main_page),
	path('product/<int:product_id>/', views.show_product, name = 'product'),
	path('sort/', views.sort, name = 'sort'),
	path('category/<str:category>/', views.category, name = 'category'),
	path('category/<str:category>/sort/', views.sort_in_categories, name = 'category_sort'),
]