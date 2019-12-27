from django.urls import include,path
from .views import managerApp
from .views import proposal
from .views import person
from .views import term


#app_name = 'managerApp'

urlpatterns = [

    path('', managerApp.home, name='home'),

    path('proposals/', include(([
        path('', proposal.IndexView.as_view(), name='proposals_list'),
        path('<int:pk>/', proposal.DetailView.as_view(), name='proposals_details'),
        path('create/', proposal.CreateProposalView.as_view(), name='proposals_create'),
        path('<int:pk>/update/', proposal.UpdateProposalView.as_view(), name='proposals_update'),
        path('<int:pk>/delete/', proposal.DeleteProposalView.as_view(), name='proposals_delete')
    ], 'managerApp'), namespace='proposals')),

    path('persons/', include(([
        path('', person.IndexView.as_view(), name='persons_list'),
        path('<int:pk>/', person.DetailView.as_view(), name='persons_details'),
        path('create/', person.CreatePersonView.as_view(), name='persons_create'),
        path('<int:pk>/update/', person.UpdatePersonView.as_view(), name='persons_update'),
        path('<int:pk>/delete/', person.DeletePersonView.as_view(), name='persons_delete')
    ], 'managerApp'), namespace='persons')),


    path('term/', include(([
        path('', term.IndexView.as_view(), name='terms_list'),
        path('create/', term.CreateTermView.as_view(), name='terms_create'),
        path('<int:pk>/update/', term.UpdateTermView.as_view(), name='terms_update'),
        path('<int:pk>/delete/', term.DeleteTermView.as_view(), name='terms_delete')
    ], 'managerApp'), namespace='terms')),

    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:propuesta_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:propuesta_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:propuesta_id>/modify/', views.modify, name='modify'),
]
