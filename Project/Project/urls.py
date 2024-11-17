# Project/urls.py
from django.contrib import admin
from django.urls import path, include
from survey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.survey_show, name='survey_show'),  # Handle root URL
    path('Project/survey/output/', views.survey_output, name='survey_output'),  # Survey output URL
]
