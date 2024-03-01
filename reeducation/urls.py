
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include("admins.urls",namespace="main")),
    path('',include("student.urls",namespace="student"))
]
