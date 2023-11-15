from django.test import TestCase
from rest_framework import status

from .views import get_form
from forms_app.models import FormField, FormTemplate


class TestGetForm(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FormTemplate.objects.create(
            name='Тестовая форма',
        )
        cls.field_date = FormField.objects.create(
            template=cls.form,
            name='Дата',
            type='date',
        )
        cls.field_phone = FormField.objects.create(
            template=cls.form,
            name='Телефон',
            type='phone',
        )
        cls.field_email = FormField.objects.create(
            template=cls.form,
            name='Почта',
            type='email',
        )
        cls.field_text = FormField.objects.create(
            template=cls.form,
            name='Текст',
            type='text',
        )


    def test_get_form(self):
        form_data = {
            'Текст': 'текст',
            'Почта': 'john@example.com',
            'Телефон': '+7 123 456 78 90',
            'Дата': '2022-01-01'
        }
        response = self.client.post('/get_form/', form_data, format='json')
        request = response.wsgi_request
        form_response = get_form(request)
        self.assertEqual(form_response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'Тестовая форма')


    def test_not_existing_form(self):
        form_data = {
            'Текст': 'текст',
            'Почта': 'john@example.com',
            'Телефон': '+7 123 456 78 90',
            'Неизвестное поле': '2022-01-01'
        }
        response = self.client.post('/get_form/', form_data, format='json')
        request = response.wsgi_request
        form_response = get_form(request)
        self.assertEqual(form_response.status_code, status.HTTP_200_OK)
        response_form = {
            'Текст': 'text',
            'Почта': 'email',
            'Телефон': 'phone',
            'Неизвестное поле': 'date'
        }
        self.assertEqual(response.data, response_form)
