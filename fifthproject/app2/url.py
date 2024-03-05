from app2 import views
from django.urls import path
urlpatterns = [
    path('new2/',views.pat1),
    path('msg2/',views.patview,name="patient"),
    path('update1/<int:pk>/',views.doc2,name="update_pat"),
    path('delete1/<int:pk>/',views.delete,name="delete_pat")
]