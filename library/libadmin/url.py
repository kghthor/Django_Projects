from libadmin import views
from django.urls import path
urlpatterns = [
    path('new1/',views.doc1,name="reg1"),
    path('msg1/',views.docview,name="viewmsg"),
    path('page/',views.stamod,name="index"),
    path('page/serv/',views.serv,name="service"),
    path('page/about/',views.abt,name="about"),
    path('page/team/',views.tem,name="team"),
    path('page/why/',views.wh,name="why")
]