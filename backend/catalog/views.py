from django.shortcuts import render, get_object_or_404
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "catalog/project_detail.html", {"project": project})

def main(request):
    return render(request, "catalog/main.html")