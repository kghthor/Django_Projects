from app1 import views
from django.urls import path
urlpatterns = [
    path('new1/',views.doc1,name="doco"),
    path('msg1/',views.docview,name="docview"),
    path('update/<int:pk>/',views.doc2,name="update_doc"),
    path('delete/<int:pk>/',views.delete,name="delete_doc")
]