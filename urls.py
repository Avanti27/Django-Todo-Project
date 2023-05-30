from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_course,name="get_course"),
    path('index',views.index,name="index"),
    path('home',views.home,name="name"),
    path('contact', views.contact,name="contact"),
    path('placement', views.placement,name="placement"),
    path('create',views.create,name="create"),
    path('store',views.store,name="store"),
    path('create',views.create,name="create"),
    path('form',views.getform,name="getform"),
    path('course',views.courseform,name="courseform"),
    path('create_course',views.create_course,name="create_course"),
    path('',views.get_course,name="get_course"),
    path('delete/<rid>',views.delete,name="delete"),
    path('edit/<rid>',views.edit,name="edit"),
    path('filter_records',views.filter_records,name="filter"),
    path('showform',views.showformdata,name="showform"),
    path('signup',views.register,name="user_register"),
    path('login',views.user_login,name="user_login"), 
    path('profile',views.user_profile,name="user_profile"),
    path('logout',views.user_logout,name="user_logout"),
    path('home/<name>',views.name,name="name"), 
    path('setcookie',views.set_cookie,name="setcookie"),
    path('getcookie',views.get_cookie,name="getcookie"),
    path('delcookie',views.del_cookie,name="delcookie"),
    path('setsession',views.set_session,name='set_session'),
    path('getsession',views.get_session,name='get_session'),
    path('delsession',views.del_session,name='del_session'),
    path('home',views.home),

]
