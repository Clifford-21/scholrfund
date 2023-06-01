from django.urls import path
from . import views

urlpatterns = [
    path("learners/", views.show_learners),
    path("learners/<int:id>/", views.show_learner),
]
