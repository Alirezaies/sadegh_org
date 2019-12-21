from django.test import TestCase
from django.urls import(
    resolve,
    reverse
)

from ..controllers.home import HomeView
from ..models import *

class HomeTest(TestCase):
    def setUp(self):
        Bio.objects.create(bio='this is a test bio!')
        self.home_view = HomeView().home_controller

    def home_url_resolves_resolves_home_func(self):
        url = reverse('home')
        view = resolve(url)

        self.assertEquals(view.func, self.home_view)

    def test_home_view_status_code_404_on_no_bio(self):
        """ no bio added to the database """
        Bio.objects.get(id=1).delete()
        url = reverse('home')
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 404)

    def test_home_view_status_code_200(self):
        Bio.objects.create(bio='this is a test bio!')
        url = reverse('home')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_home_view_contains_langs(self):
        Language.objects.create(name='Persian', level='Native')

        url = reverse('home')
        response = self.client.get(url)

        self.assertContains(response, 'Persian <span>(Native)</span>')

    def test_home_view_link_to_social_media(self):
        SocialLinks.objects.create(name='Facebook', link='https://fb.com/AlirezaieS', icon_class='fa fa-facebook')
        facebook_link = SocialLinks.objects.get(link='https://fb.com/AlirezaieS').link

        url = reverse('home')
        response = self.client.get(url)

        self.assertContains(response, 'href="{0}"'.format(facebook_link))
        self.assertContains(response, 'class="fa fa-facebook"')
    
    def test_home_view_contains_specialities(self):
        Specialities.objects.create(name='test name', desc='test desc')

        url = reverse('home')
        response = self.client.get(url)

        self.assertContains(response, '<h3>test name</h3>')
        self.assertContains(response, '<p>test desc</p>')
