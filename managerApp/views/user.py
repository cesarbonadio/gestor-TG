from . import *
import itertools


#sin contraseña para agregarla solo en la creación
USER_CRUD_FIELDS = [
    "username",
    "first_name",
    "last_name",
    "email",
    "is_active",
    "date_joined",
    "is_admin",
    "is_manager",
    "is_guest"
]

#evitar sobreescritura de la instancia "user" de las sesiones
USER_CRUD_CONTEXT_OBJECT_NAME = "user_context_object"


@method_decorator([login_required, admin_permissions], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'managerApp/user/index.html'
    context_object_name = 'users_list'
    
    def get_queryset(self):
        return User.objects.order_by('id')
        

@method_decorator([login_required, admin_permissions], name='dispatch')
class DetailView(generic.DetailView):
    model = User
    template_name = 'managerApp/user/detail.html'
    context_object_name = USER_CRUD_CONTEXT_OBJECT_NAME


@method_decorator([login_required, admin_permissions], name='dispatch')
class CreateUserView(generic.CreateView):
    model = User
    CREATE_FIELDS = USER_CRUD_FIELDS.copy()
    CREATE_FIELDS.insert(0,'password')
    fields = CREATE_FIELDS
    template_name = 'managerApp/user/create.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save_hashing()
        messages.success(self.request, 'Fue creado un nuevo usuario')
        return redirect('user:user_list')



@method_decorator([login_required, admin_permissions], name='dispatch')
class UpdateUserView(generic.UpdateView):
    model = User
    fields = USER_CRUD_FIELDS
    template_name = 'managerApp/user/update.html'
    context_object_name = USER_CRUD_CONTEXT_OBJECT_NAME

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save_without_hashing()
        messages.success(self.request, 'Fue actualizado un usuario')
        return redirect('user:user_list')


@method_decorator([login_required, admin_permissions], name='dispatch')
class DeleteUserView(generic.DeleteView):
    model = User
    template_name = 'managerApp/user/delete.html'
    success_url = reverse_lazy('user:user_list')
    context_object_name = USER_CRUD_CONTEXT_OBJECT_NAME

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Usuario eliminado exitosamente")
        return super().delete(request, *args, **kwargs)



@login_required
@admin_permissions
def LogsTransacciones(request):
    
    actions_executed_persons = Person.history.all()
    actions_executed_defense = Defense.history.all()
    actions_executed_persontype = PersonType.history.all()
    actions_executed_proposals = Proposal.history.all()
    actions_executed_proposalsstatus = ProposalStatus.history.all()
    actions_executed_term = Term.history.all()
    actions_executed_thesisstatus = ThesisStatus.history.all()
    actions_executed_thesis = Thesis.history.all()

    actions_executed = list(itertools.chain(
        actions_executed_persons, 
        actions_executed_defense, 
        actions_executed_persontype,
        actions_executed_proposals,
        actions_executed_proposalsstatus,
        actions_executed_term,
        actions_executed_thesisstatus,
        actions_executed_thesis
    ))

    return render(request, 'managerApp/reporte/logporusuario/index.html', {'actions_executed':actions_executed})
