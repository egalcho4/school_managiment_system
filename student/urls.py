from django.urls import path
from . import views
app_name="student"
urlpatterns=[
    path('',views.logina,name="login"),
    path('home/',views.home,name="home")
]