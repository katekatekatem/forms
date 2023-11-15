from django import forms

from .models import FormTemplate, FormField


class FormTemplateForm(forms.ModelForm):
    class Meta:
        model = FormTemplate
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Form template name'

        for field_name, field_type in self.fields.iteritems():
            field = FormField(name=field_name, type=field_type)
            self.form_fields.append(field)


class FormFieldForm(forms.ModelForm):
    class Meta:
        model = FormField
        fields = ('name', 'type')
