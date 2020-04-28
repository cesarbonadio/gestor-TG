from django import template


def translate_model_name(model_name):

    value_type = model_name.lower()
    
    if value_type == "proposal":
        return "propuesta"
    elif value_type == "person":
        return "persona"
    elif value_type == "personType":
        return "tipo de persona"
    elif value_type == "term":
        return "terminología"
    elif value_type == "thesisStatus":
        return "estatus de tesis"
    elif value_type == "proposalStatus":
        return "estatus de propuesta"
    elif value_type == "defense":
        return "defensa"
    elif value_type == "thesis":
        return "tesis"


register = template.Library()
@register.filter
def get_type(value):
    value_type = value.__class__.__name__
    return translate_model_name(value_type)


@register.filter
def get_related_objects(value):
    related_objects_list = []
    for field in value._meta.get_fields():
        if field.one_to_many:
            related_objects_list.append(field.name.split('_')[1])
    return ','.join([translate_model_name(model_name) for model_name in related_objects_list])