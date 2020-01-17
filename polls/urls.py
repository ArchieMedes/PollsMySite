from django.urls import path
from . import views


# app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name = 'index'),
#     path('especificaciones/<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/resultados/', views.results, name='results'),
#     path('<int:question_id>/votar/', views.vote, name='vote'),
# ]

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/resultados/', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/votar/', views.vote, name = 'vote'),
]