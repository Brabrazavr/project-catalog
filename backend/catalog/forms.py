from django import forms
from .models import Project, Tag

class ProjectFilterForm(forms.Form):
    title = forms.CharField(label="Название", required=False)
    year = forms.ChoiceField(label="Учебный год", choices=[("", "Все")] + Project.YEAR_CHOICES, required=False)
    project_type = forms.ChoiceField(label="Тип проекта", choices=[("", "Все")] + Project.PROJECT_TYPE_CHOICES, required=False)
    author = forms.CharField(label="Автор", required=False)
    supervisor = forms.CharField(label="Супервайзер", required=False)
    level = forms.ChoiceField(label="Уровень", choices=[("", "Все")] + Project.LEVEL_CHOICES, required=False)
    scale = forms.ChoiceField(label="Масштаб", choices=[("", "Все")] + Project.SCALE_CHOICES, required=False)
    perspectives = forms.ChoiceField(label="Перспективы", choices=[("", "Все"), ("Yes", "Да"), ("No", "Нет")], required=False)
    customer = forms.ChoiceField(label="Заказчик", choices=[("", "Все"), ("Inner", "Внутренний"), ("Outer", "Внешний"), ("Not stated", "Не указано")], required=False)

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,  # можно использовать Checkbox или SelectMultiple
        label="Теги"
    )