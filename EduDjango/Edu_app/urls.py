from django.urls import path
from . import views
from .views import create_stream, stream_list
urlpatterns=[
 path('', views.home, name='home'),
 path('dashboard/',views.dashboard, name='dashboard'),
 path('career_test/',views.career_test, name='career_test'),
 path('subjects/',views.subjects,name='subjects'),
 path('users/',views.users,name='users'),
 path('navstream/',views.navstream,name='navstream'),
 path('stream',views.stream,name='stream'),
  path('streams/', stream_list, name='stream_list'),
path('streams/create/', create_stream, name='create_stream'),
 
]