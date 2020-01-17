from django.db import models

# Create your models here.

import datetime
from django.utils import timezone

#Para crear MODELOS se hace mediante la definición de CLASES

#Para la aplicación de ENCUESTA (polls) necesitamos crear DOS MODELOS:
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #Vamos a AGREGAR un MÉTODO para poder visualizar mejor desde el SHELL de PYTHON los OBJETOS de tipo QUESTION y CHOICE:
    def __str__(self):
        return self.question_text
    #Vamos a AGREGAR también un MÉTODO PERONSALIZADO para este MODELO:
    #Para ello necesitamos importar "DATETIME" y "TIMEZONE"
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

#El segundo MODELO (CHOICE) estará relacionado con el primero mediante una LLAVE FORANEA:
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #Vamos a AGREGAR un MÉTODO para poder visualizar mejor desde el SHELL de PYTHON los OBJETOS de tipo QUESTION y CHOICE:
    def __str__(self):
        return self.choice_text
    





