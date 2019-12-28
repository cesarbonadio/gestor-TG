from django.urls import include,path
from .views import managerApp
from .views import proposal
from .views import person
from .views import term
from .views import proposalstatus
from .views import thesisstatus
from .views import thesis



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

    path('proposalstatus/', include(([
        path('', proposalstatus.IndexView.as_view(), name='proposal_status_list'),
        path('create/', proposalstatus.CreateProposalStatusView.as_view(), name='proposal_status_create'),
        path('<int:pk>/update/', proposalstatus.UpdateProposalStatusView.as_view(), name='proposal_status_update'),
        path('<int:pk>/delete/', proposalstatus.DeleteProposalStatusView.as_view(), name='proposal_status_delete'),
    ], 'managerApp'), namespace='proposal_status')),

    path('thesisstatus/', include(([
        path('', thesisstatus.IndexView.as_view(), name='thesis_status_list'),
        path('create/', thesisstatus.CreateThesisStatusView.as_view(), name='thesis_status_create'),
        path('<int:pk>/update/', thesisstatus.UpdateThesisStatusView.as_view(), name='thesis_status_update'),
        path('<int:pk>/delete/', thesisstatus.DeleteThesisStatusView.as_view(), name='thesis_status_delete'),
    ], 'managerApp'), namespace='thesis_status')),

    path('thesis/', include(([
        path('', thesis.IndexView.as_view(), name='thesis_list'),
        path('create/', thesis.CreateThesisView.as_view(), name='thesis_create'),
        path('<str:pk>/', thesis.DetailView.as_view(), name='thesis_details'),
        path('<str:pk>/update/', thesis.UpdateThesisView.as_view(), name='thesis_update'),
        path('<str:pk>/delete/', thesis.DeleteThesisView.as_view(), name='thesis_delete'),
    ], 'managerApp'), namespace='thesis'))

    


]
