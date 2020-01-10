from django.urls import include,path
from .views import managerApp,proposal,person,term,proposalstatus,thesisstatus,thesis,defense,persontype,user,pdf


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
    ], 'managerApp'), namespace='thesis')),

    path('defense/', include(([
        path('', defense.IndexView.as_view(), name='defense_list'),
        path('create/', defense.CreateDefenseView.as_view(), name='defense_create'),
        path('<str:pk>/', defense.DetailView.as_view(), name='defense_details'),
        path('<str:pk>/update/', defense.UpdateDefenseView.as_view(), name='defense_update'),
        path('<str:pk>/delete/', defense.DeleteDefenseView.as_view(), name='defense_delete'),
    ], 'managerApp'), namespace='defense')),

    path('persontype/', include(([
        path('', persontype.IndexView.as_view(), name='person_type_list'),
        path('create/', persontype.CreatePersonTypeView.as_view(), name='person_type_create'),
        path('<int:pk>/update/', persontype.UpdatePersonTypeView.as_view(), name='person_type_update'),
        path('<int:pk>/delete/', persontype.DeletePersonTypeView.as_view(), name='person_type_delete'),
    ], 'managerApp'), namespace='person_type')),

    path('users/', include(([
        path('', user.IndexView.as_view(), name='user_list'),
        path('create/', user.CreateUserView.as_view(), name='user_create'),
        path('<int:pk>/', user.DetailView.as_view(), name='user_details'),
        path('<int:pk>/update/', user.UpdateUserView.as_view(), name='user_update'),
        path('<int:pk>/delete/', user.DeleteUserView.as_view(), name='user_delete'),
    ], 'managerApp'), namespace='user')),

    path('reporte/', include(([
        path('propsinaprobar', proposal.PropuestasSinAprobarView.as_view(), name='propsinaprobar'),
        path('propsinaprobar/<int:pk>/', proposal.PropuestasSinAprobarDetailView.as_view(), name='propsinaprobar_details'),
        path('tgenejecucion', thesis.ThesisEnEjecucionView.as_view(), name='tgenejecucion'),
        path('defensapendiente', defense.DefensaPendienteView.as_view(), name='defensapendiente'), 
        path('actporstatus', term.ActPorStatusView.as_view(), name='actporstatus'), 
        path('asignadoaprofesor', person.SelectorDeReporteView.as_view(), name='asignadoaprofesor'), 
        path('tareasdeprofesor', person.TareasPorProfesorView.as_view(), name='tareasdeprofesor'), 
        path('actporterminologia', term.SelectorTermView.as_view(), name='actporterminologia'), 
        path('tareasporterm', term.TareasPorTermView.as_view(), name='tareasporterm'), 
        path('estadisticas', defense.TermSelectorView.as_view(), name='estadisticas'),
        path('data/estadisticas', defense.TermSelectorView.get_data, name='data_estadisticas'),
        path('logstransacciones', user.LogsTransacciones, name="log_transacciones")
    ], 'managerApp'), namespace='reporte')),

    path('pdf/', include(([
        #PDF de reportes
        path('actporterminologia',pdf.ActPorTerm.as_view(),name='pdf_actporterminologia'),
        path('actporterminologia_detalle',pdf.ActPorTermDet.as_view(),name='pdf_actporterminologiadet'),
        path('estadisticas_notas',pdf.StatsNotas.as_view(),name='pdf_estadisticas_notas'),
        path('tareasdeprofesor',pdf.TareasProfesor.as_view(),name='pdf_tareasdeprofesor'),
        path('tareasdeprofesor_detalle',pdf.TareasProfesorDetalle.as_view(),name='pdf_tareasdeprofesordet'),
        path('defensapendiente',pdf.DefensasPendientes.as_view(),name='pdf_defensapendiente'),
        path('defensapendiente_detalle',pdf.DefensasPendientesDetalle.as_view(),name='pdf_defensapendientedet'),
        path('tgenejecucion',pdf.TgEjecucion.as_view(),name='pdf_tgenejecucion'),
        path('tgenejecucion_detalle',pdf.TgEjecucionDetalle.as_view(),name='pdf_tgenejecuciondet'),
        path('propsinaprobar',pdf.PropuestasSinAprobar.as_view(),name='pdf_propsinaprobar'),
        path('propsinaprobar_detalle',pdf.PropuestasSinAprobarDetalle.as_view(),name='pdf_propsinaprobardet'),
        path('actporstatus', pdf.ActPorStatus.as_view(), name='pdf_actporstatus'), 
        path('actporstatus_detalle', pdf.ActPorStatusDetalle.as_view(), name='pdf_actporstatus_detalle'), 
        path('logstransacciones', pdf.LogsTransacciones.as_view(), name="pdf_log_transacciones"),

        #PDF de consultas
        path('proposal',pdf.ProposalIndex.as_view(),name='pdf_proposal'),
        path('person',pdf.PersonIndex.as_view(),name='pdf_person'),
        path('term',pdf.TermIndex.as_view(),name='pdf_term'),
        path('thesis',pdf.ThesisIndex.as_view(),name='pdf_thesis'),
        path('defense',pdf.DefenseIndex.as_view(),name='pdf_defense'),
    ], 'managerApp'), namespace='pdf'))

]
 