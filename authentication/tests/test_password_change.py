from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginRequiredPasswordChangeTests(TestCase):
    def test_redirection(self):
        url = reverse('change_password')
        login_url = reverse('login')
        response = self.client.get(url)

        self.assertRedirects(response, f'{login_url}?next={url}')

class PasswordChangeTestCase(TestCase):
    def setUp(self, data={}):
        self.user = User.objects.create_user(
            username='john',
            password='old_password1234',
            email='john@doe.com'
        )
        self.url = reverse('change_password')

        self.client.login(
            username='john',
            password='old_password1234'
        )

        self.response = self.client.post(self.url, data)

class SuccessfulPasswordChangeTests(PasswordChangeTestCase):
    def setUp(self):
        super().setUp({
            'old_password':'old_password1234',
            'new_password1':'new_pass1234',
            'new_password2':'new_pass1234',
        })

    def test_redirection(self):
        """ valid form submission should redirect the user """

        url = reverse('password_change_done')

        self.assertRedirects(self.response, url)
    
    def test_password_changed(self):
        """
            refresh the user instance from the database to get the new password
            hash updated by the change passsword view
        """

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('new_pass1234'))

    def test_user_authentication(self):
        """
            create a new request to an arbitary page
            the resulting response should now have an 'user' to its context,
            after a succeesful signup...
        """

        response = self.client.get(reverse('home'))
        user = response.context.get('user')

        self.assertTrue(self.user.is_authenticated)

class InvalidPasswordChangeTest(PasswordChangeTestCase):
    def test_status_code(self):
        """
            invalid form submission should return to the same page
        """

        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')

        self.assertTrue(form.errors)

    def test_password_not_changed(self):
        self.user.refresh_from_db()

        self.assertTrue(self.user.check_password('old_password1234'))
