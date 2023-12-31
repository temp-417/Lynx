from django.test import TestCase
from tasks.models import User
from tasks.forms import RemoveMemberForm

class RemoveMemberFormTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='USER1', email='test@example.com', password='Subject6')
        self.form_input = {'email': 'test@example.com'}

    def test_valid_email(self):
        form = RemoveMemberForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_blank_email(self):
        self.form_input['email'] = ''
        form = RemoveMemberForm(data=self.form_input)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_invalid_email(self):
        self.form_input['email'] = 'ichbinkrankenhouse@example.com'
        form = RemoveMemberForm(data=self.form_input)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['No user found with this email address.'])

    def test_clean_email_method(self):
        form = RemoveMemberForm(data = {'email': 'test@example.com'})
        form.cleaned_data = {'email': 'test@example.com'}
        cleaned_email = form.clean()
        self.assertEqual(cleaned_email.get('email'), 'test@example.com')

    def test_email_exist_in_database_method(self):
        form = RemoveMemberForm()
        email_exists = form.email_exist_in_database('test@example.com')
        self.assertTrue(email_exists)

        email_exists = form.email_exist_in_database('ichbinkrankenhouse@example.com')
        self.assertFalse(email_exists)