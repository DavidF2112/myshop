from django.urls import path
from .views import *
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>' , views.product_detail,name='product_detail'),
]
