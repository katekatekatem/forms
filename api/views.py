from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from forms_app.models import FormTemplate
from forms_app.validators import (
    validate_date, validate_email, validate_phone,
)


@api_view(['POST'])
def get_form(request):
    form_data = request.data

    field_types = {}
    for field_name, field_value in form_data.items():
        if isinstance(field_value, str):
            if validate_date(field_value):
                field_types[field_name] = 'date'
            elif validate_phone(field_value):
                field_types[field_name] = 'phone'
            elif validate_email(field_value):
                field_types[field_name] = 'email'
            else:
                field_types[field_name] = 'text'
        else:
            return Response(
                {'detail': f'Неизвестный формат поля формы "{field_name}"'},
                status=status.HTTP_400_BAD_REQUEST
            )

    form_templates = FormTemplate.objects.all()
    for template in form_templates:
        template_fields = template.formfield_set.all()

        match = True
        for field in template_fields:
            field_name = field.name
            field_type = field.type

            if (field_name not in form_data) or (
                field_types[field_name] != field_type
            ):
                match = False
                break

        if match:
            return Response(template.name)

    return Response(field_types)
