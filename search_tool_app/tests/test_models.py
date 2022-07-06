from django.test import TestCase
from search_tool_app.models import *

# class ModelTypeTest(TestCase):
#     def setUp(self):
#         self.data1 = Type.objects.create(type="hateveererere")

#     def test_type_model_test(self):
#         '''
#         simple example structure of test
#         '''
#         data = self.data1
#         self.assertTrue(isinstance(data, Type))

class ModelTypeTest(TestCase):
    def setUp(self):
        self.data1 = Type.objects.create(type="hateveererere")

    def test_type_model_test(self):
        '''
        Test Type model returned type
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Type))
        self.assertEqual(str(data), "hateveererere")

class ModelLanguageTest(TestCase):

    def setUp(self):
        self.data1 = Language.objects.create(language="English")

    def test_language_model_test(self):
        '''
        Test Language model returned type
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Language))
        self.assertEqual(str(data), "English")        