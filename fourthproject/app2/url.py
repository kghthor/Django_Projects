from app2 import views
from django.urls import path
urlpatterns = [
    path('new2/',views.view2),
    path('msg/',views.view3)
]