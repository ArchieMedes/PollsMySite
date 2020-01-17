# Create your views here.

# Para crear una VISTA que haga realmente algo con la función VOTE 
# necesitamos IMPORTAR el HttpResponseRedirect aquí abajo, además del ya utilizado HttpResponse: 
# from django.http import HttpResponse, HttpResponseRedirect

# Para poder CARGAR una PLANTILLA importaremos la siguiente biblioteca:
# La usamos sólo para la VISTA mejorada USANDO una PLANTILLA
# from django.template import loader

# Importamos el ERROR 404
#from django.http import Http404

# Para cargar una VISTA usando PLANTILLAS con RENDER()
#from django.shortcuts import render

# Para cargar una VISTA usando PLANTILLAS con RENDER() y usando el SHORTCUT get_object_or_404():
# from django.shortcuts import get_object_or_404, render

# Agregamos para crear una VISTA que haga realmente algo con la función VOTE:
# from django.urls import reverse

# Para modificar la VISTA de index() vamos a importar el modelo QUESTION, y para modificar la VISTA de VOTE importamos el modelo CHOICE:
# from .models import Question, Choice

# ---------------------------------------------------------------------------------

"""

def index(request):

    # Vista ORIGINAL y la más simple posible:
    #return HttpResponse("Hola, mundo. Estás en el ÍNDICE de la ENCUESTA")

    # Vista MEJORADA:
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # Vista MEJORADA USANDO una PLANTILLA
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # Vista MEJORADA aún más USANDO una PLANTILLA y RENDER()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Definición SENCILLA de la VISTA de "DETAIL"
# def detail(request, question_id):
#    return HttpResponse("Estás viendo la pregunta número %s." % question_id)

def detail(request, question_id):

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("La pregunta que solicitaste NO existe. 'tas todo estúpido, mijo...")
    # return render(request, 'polls/detail.html', {'question': question})

    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):

    # response = "Estás viendo los resultados de la pregunta número %s."
    # return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

"""
# ------------------------------------------------------------------------------------------    

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
#Importamos de VIEWS la biblioteca GENERIC
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Retorna las últimas 5 preguntas publicadas."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):

    # return HttpResponse("Estás votando en la pregunta número %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Vuelve a desplegar el formulario:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "No seleccionaste ninguna opción, simio.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre retorna un HttpResponseRedirect después de tratar con éxito
        # el POST data. Esto previene que tus datos sean pasados dos veces si un usuario 
        # pica el botón de regreso.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))