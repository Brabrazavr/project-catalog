from django.urls import path
from django.contrib.auth import views as auth_views
from .views import project_detail, main
from .views import project_list


urlpatterns = [
    path("", main, name="main"),
    path("project/<int:pk>/", project_detail, name="project_detail"),
    path("login/", auth_views.LoginView.as_view(template_name="catalog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("projects/", project_list, name="project_list"),
]
