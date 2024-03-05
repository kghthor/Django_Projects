from firstapp import views
from django.urls import  path

urlpatterns = [
    path('', views.display),
    path('add/',views.add),
    path('sub/',views.sub),
    path('displa/',views.displa),
    path('dispy/',views.dispy)
]