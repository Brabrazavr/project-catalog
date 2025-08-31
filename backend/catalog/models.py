from django.db import models
from django.views.generic import ListView

class Project(models.Model):
    title = models.CharField("Название проекта", max_length=255)

    YEAR_CHOICES = [
        ("2018-2019", "2018–2019"),
        ("2019-2020", "2019–2020"),
        ("2020-2021", "2020–2021"),
        ("2021-2022", "2021–2022"),
        ("2022-2023", "2022–2023"),
        ("2023-2024", "2023–2024"),
        ("2024-2025", "2024–2025"),
        ("2025-2026", "2025–2026"),
        ("2026-2027", "2026–2027"),
        ("2027-2028", "2027–2028"),
    ]
    year = models.CharField("Учебный год", max_length=9, choices=YEAR_CHOICES)

    PROJECT_TYPE_CHOICES = [
        ("social", "Социальный"),
        ("personal", "Персональный"),
        ("ivr", "ИВР"),
    ]
    project_type = models.CharField("Тип проекта", max_length=10, choices=PROJECT_TYPE_CHOICES, default="")

    author = models.CharField("Автор проекта", max_length=255)

    supervisor = models.CharField("Супервайзер", max_length=255)

    LEVEL_CHOICES = [
        ("low", "Минимальный"),
        ("basic", "Базовый"),
        ("high", "Высокий"),
    ]
    level = models.CharField("Уровень проекта", max_length=10, choices=LEVEL_CHOICES, default="")

    SCALE_CHOICES = [
        ("school", "Школьный"),
        ("city", "Городской"),
        ("regional", "Региональный"),
        ("national", "Всероссийский"),
    ]
    scale = models.CharField("Масштаб проекта", max_length=15, choices=SCALE_CHOICES, default="")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"{self.title} ({self.year})"
