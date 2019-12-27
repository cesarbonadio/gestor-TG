from django.urls import include,path
from .views import managerApp
from .views import proposal
from .views import person


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
    ], 'managerApp'), namespace='persons')),

    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:propuesta_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:propuesta_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:propuesta_id>/modify/', views.modify, name='modify'),
]
