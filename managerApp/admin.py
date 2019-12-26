from django.contrib import admin
from .models import Person
from .models import Term
from .models import ProposalStatus
from .models import ThesisStatus
from .models import Proposal
from .models import Thesis
from .models import Defense

'''TODO-> ver si realmente es necesario el sitio de administrador'''

# Para el site de administrador.
admin.site.register(Person)
admin.site.register(Term)
admin.site.register(ProposalStatus)
admin.site.register(ThesisStatus)
admin.site.register(Proposal)
admin.site.register(Thesis)
admin.site.register(Defense)