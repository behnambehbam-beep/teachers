from django.urls import path
from app_teachers.api import views

urlpatterns = [
    path('page-subject/', views.page_subject),
    path('page-title/', views.page_title),
    path('about-us/', views.about_us),
    path('our-services/', views.our_services),
    path('education-category/', views.education_category),
    path('course-table/', views.course_table),
    path('course-schedule/', views.course_schedule),
    path('image-ourclasses/', views.image_ourclasses),
]