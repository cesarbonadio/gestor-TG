from django import forms
from .models import *
from bootstrap_datepicker_plus import DateTimePickerInput

class ProposalForm(forms.ModelForm):

    delivery_date=forms.DateTimeField(
            widget=DateTimePickerInput(
                options={
                    "format": "DD/MM/YYYY hh:mm:ss"
                }
            )
        )

    class Meta:
       model = Proposal
       fields = "__all__"