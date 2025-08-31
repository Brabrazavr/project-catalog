from django.urls import path
from django.contrib.auth import views as auth_views
from .views import project_detail, main, project_list, save_project, remove_project, selected_projects

urlpatterns = [
    path("", main, name="main"),
    path("project/<int:pk>/", project_detail, name="project_detail"),
    path("login/", auth_views.LoginView.as_view(template_name="catalog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("projects/", project_list, name="project_list"),
    path("project/<int:pk>/save/", save_project, name="save_project"),
    path("project/<int:pk>/remove/", remove_project, name="remove_project"),
    path("selected/", selected_projects, name="selected_projects"),
]
