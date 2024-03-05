from myapp import views
from django.urls import path

urlpatterns = [
    path('party/',views.party),
    path('p/',views.part)
]