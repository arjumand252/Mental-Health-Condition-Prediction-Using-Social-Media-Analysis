from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.survey_show, name='survey_show'),
    path('survey/output/', views.survey_output, name='survey_output'),  # URL for the output page
]
