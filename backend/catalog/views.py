from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectFilterForm


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "catalog/project_detail.html", {"project": project})

@login_required
def main(request):
    return render(request, "catalog/main.html")


@login_required
def project_list(request):
    projects = Project.objects.all()
    form = ProjectFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data["title"]:
            projects = projects.filter(title__icontains=form.cleaned_data["title"])
        if form.cleaned_data["year"]:
            projects = projects.filter(year=form.cleaned_data["year"])
        if form.cleaned_data["project_type"]:
            projects = projects.filter(project_type=form.cleaned_data["project_type"])
        if form.cleaned_data["author"]:
            projects = projects.filter(author__icontains=form.cleaned_data["author"])
        if form.cleaned_data["supervisor"]:
            projects = projects.filter(supervisor__icontains=form.cleaned_data["supervisor"])
        if form.cleaned_data["level"]:
            projects = projects.filter(level=form.cleaned_data["level"])
        if form.cleaned_data["scale"]:
            projects = projects.filter(scale=form.cleaned_data["scale"])
        if form.cleaned_data["perspectives"]:
            projects = projects.filter(perspectives=form.cleaned_data["perspectives"])
        if form.cleaned_data["customer"]:
            projects = projects.filter(customer=form.cleaned_data["customer"])

    return render(request, "catalog/project_list.html", {"form": form, "projects": projects})

@login_required
def save_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    request.user.saved_projects.add(project)
    return redirect("project_detail", pk=pk)

@login_required
def remove_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    request.user.saved_projects.remove(project)
    return redirect("selected_projects")

@login_required
def selected_projects(request):
    projects = request.user.saved_projects.all()
    return render(request, "catalog/selected_projects.html", {"projects": projects})