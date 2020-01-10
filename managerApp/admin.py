from django.contrib import admin
from .models import *


# Para el site de administrador.
admin.site.register(Person)
admin.site.register(Term)
admin.site.register(ProposalStatus)
admin.site.register(ThesisStatus)
admin.site.register(Proposal)
admin.site.register(Thesis)
admin.site.register(Defense)
admin.site.register(PersonType)
admin.site.register(User)