from django.urls import path
from app_teachers.api import views

urlpatterns = [
    path('page-subject/', views.page_subject),
    path('page-title/', views.page_title),
    path('about-us/', views.about_us),
]