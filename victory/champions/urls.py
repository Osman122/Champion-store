from django.urls import path 
from champions.views import index, about ,contact ,show,delete,filter,add,edit,category_list,category_detail
from champions.api.views import indexx ,product_resource

urlpatterns = [
    path('home',index, name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('product/<int:id>',show , name='champion.product'),
    path('product/<int:id>/delete',delete , name='product.delete'),
    path('search', filter , name='search'),
    path('forms/create',add,name='add'),
    path('forms/edit/<int:id>', edit, name='edit'),
    path('category_list',category_list,name='category_list'),
    path('category/<str:category>/', category_detail, name='category_detail'),
    ###################################################api##############
    path('api', indexx, name='api.index'),
    path('api/<int:id>',product_resource,name="api.product")

] 
