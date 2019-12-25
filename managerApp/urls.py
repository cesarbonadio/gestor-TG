from django.urls import path
from . import views

app_name = 'propuestas'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:propuesta_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:propuesta_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:propuesta_id>/modify/', views.modify, name='modify'),
]
