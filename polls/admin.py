from django.contrib import admin

# Register your models here.

# Importamos del mismo "POLLS" (por eso el "punto") la clase "Question"
from .models import Question
# Le damos capacidad al administrador de poder registrar nuevos OBJETOS de tipo QUESTION
admin.site.register(Question)
