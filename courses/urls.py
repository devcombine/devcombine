from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:series_id>/', views.series_course, name='series_course'),
    path('<int:course_id>/likes', views.like_course, name='like_course'),
    path('<int:course_id>/dislikes', views.dislike_course, name='dislike_course'),
    path('<int:course_id>/likes/check',
         views.check_course_like, name='check_course_like'),
    path('likes', views.user_wishlist, name='user_wishlist'),

]
