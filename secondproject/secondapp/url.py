from secondapp import views
from django.urls import path

urlpatterns = [
    path('greeting/',views.greeting),
    path('greetin/',views.greetin),
    path('greeti/',views.greeti),
    path('greet/',views.greet)
]