from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name="about"),
    path('news/',views.news,name="news"),
    path('contact/',views.contact,name='contact'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


]