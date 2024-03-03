from django.urls import path
from . import views
app_name="main"
urlpatterns=[
    path('',views.login,name="login"),
    path('home',views.home,name="home"),
    path('acounts/',views.acounts,name="acounts"),
    path('update_users/<int:id>',views.update_users,name="update_users"),
    path('delete_users/<int:id>',views.delete_users,name="delete_users"),
    path('departiment/',views.departiment,name="departiment"),
    path('view_student/<int:id>',views.view_student,name="view_student")
]