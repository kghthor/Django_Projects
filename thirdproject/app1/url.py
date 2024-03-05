from app1 import views
from django.urls import path
urlpatterns = [
    path('new1/',views.new1),
    path('new2/',views.new2),
    path('web/',views.view1),
    path('web1/',views.view2)
]