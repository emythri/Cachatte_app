from django.urls import path
from . import views
#from .views import create_stream, stream_list
urlpatterns=[
 path('', views.home, name='home'),
 path('dashboard/',views.dashboard, name='dashboard'),
 path('career_test/',views.career_test, name='career_test'),
 #path('students', views.user_profile_view, name='students_view'),
#  path('subjects/',views.subjects,name='subjects'),
#-- path('users/',views.users,name='users'),
 path('navstream/',views.navstream,name='navstream'),
 path('subjects/<int:stream_id>/', views.subjects, name='subjects'),
 #path('stream/<int:stream_id>/subjects/', views.subjects, name='subjects'), \\\\\\
path('stream',views.stream,name='stream'),
#path('students/', views.user_profile_view, name='students_view'),
 #path('students_view/', views.user_profile_view, name='students_view'),
#path('streams/', stream_list, name='stream_list'),
# path('streams/create/', create_stream, name='create_stream'),
path('r1', views.survey_view, name='r1'),
# path('test1/<str:q1>/<str:q2>/', views.success_view, name='test1'),................
# path('result/', views.result_view, name='result'),.................
]