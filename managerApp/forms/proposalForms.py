from django import forms
from django.db import transaction
from django.forms.utils import ValidationError
from ..models import Proposal



class CreateProposalForm(forms.ModelForm):

    class Meta:
        model = Proposal
        fields = "__all__"

