from django.urls import path
from . import views
from .views import MyView,Deleteview,Searchview

urlpatterns = [
  
    path('', MyView.as_view(), name='index'),
    path('edit/<int:pk>/', MyView.as_view(), name='edit_data'),  # Edit view
    path('delete/<int:pk>/', Deleteview.as_view(), name='delete_data'),
    path('search', Searchview.as_view(), name='search'),
   
     
] 