from django import template

register = template.Library()
@register.filter
def get_type(value):

    value_type = value.__class__.__name__

    if value_type == "Proposal":
        return "propuesta"
    elif value_type == "Person":
        return "persona"
    elif value_type == "PersonType":
        return "tipo de persona"
    elif value_type == "Term":
        return "terminología"
    elif value_type == "ThesisStatus":
        return "estatus de tesis"
    elif value_type == "ProposalStatus":
        return "estatus de propuesta"
    elif value_type == "Defense":
        return "defensa"
    elif value_type == "Thesis":
        return "tesis"