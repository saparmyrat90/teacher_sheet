from django.urls import path

from . import views


urlpatterns = [
    path("", views.survey_view, name="survey_home"),
    path("get-subjects/<int:teacher_id>/", views.get_subjects, name="get_subjects"),
    path("get-questions/<str:lesson_type>/", views.get_questions, name="get_questions"),
]
