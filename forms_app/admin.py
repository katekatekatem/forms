from django.contrib import admin
from .models import FormTemplate, FormField


class FormFieldInline(admin.StackedInline):
    model = FormField
    extra = 0


@admin.register(FormTemplate)
class FormTemplateAdmin(admin.ModelAdmin):
    inlines = [FormFieldInline]


@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    pass
