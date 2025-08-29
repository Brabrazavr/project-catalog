from django.urls import path
from .views import project_detail

urlpatterns = [
    path("project/<int:pk>/", project_detail, name="project_detail"),
]