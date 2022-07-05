from urllib import response
from django.test import TestCase
from .models import *

# Create your tests here.

class Yeartest(TestCase):
    # def setUp(self):
    #     Year.objects.create(year_published="2000", convention_published="skatosundedrio", convention_venue="opou na nai")

    # def 

    def test_homepage(self):
        response =self.client.get('/')
        self.assertEqual(response.status_code, 200)

