from django.urls import path
from .import views

urlpatterns = [
    path('',views.api_overview,name='apiview'),
    path('product-list/',views.showall,name='product-list'),
    path('product-delete/<int:pk>',views.Deleteproduct,name='product-delete'),
    path('product-view/<int:pk>',views.singleprodview,name='product-view'),
    path('product-create',views.Createproduct,name='product-create'),
    path('product-update/<int:pk>',views.Updateproduct,name='product-update'),
    
]
