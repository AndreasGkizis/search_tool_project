import datetime
from django.test import TestCase
from search_tool_app.models import Year, Language, Type, Tag, Author, \
    Material, Paper, PaperUsedMaterial


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


class ModelYearTest(TestCase):

    def setUp(self):
        self.data1 = Year.objects.create(year_published=datetime.date(
            2022, 5, 24), convention_published="coven1",
            convention_venue="somethere")

    def test_year_model_test(self):
        '''
        Test year model returned type
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Year))
        self.assertEqual(str(data), "2022")
        self.assertEqual(data.year_published, datetime.date(2022, 5, 24))
        self.assertEqual(data.convention_published, "coven1")
        self.assertEqual(data.convention_venue, "somethere")


class ModelTagTest(TestCase):

    def setUp(self):
        self.data1 = Tag.objects.create(tag="onerandomtag")

    def test_tag_model_test(self):
        '''
        Test tag model returned type
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Tag))
        self.assertEqual(str(data), "onerandomtag")


class ModelmaterialTest(TestCase):

    def setUp(self):
        self.data1 = Material.objects.create(material="onerandommat")

    def test_material_model_test(self):
        '''
        Test material model returned type
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Material))
        self.assertEqual(str(data), "onerandommat")


class ModelauthorTest(TestCase):

    def setUp(self):
        self.data1 = Author.objects.create(
            name="onerandomperson",  country_of_origin="shitland")

    def test_author_model_test(self):
        '''
        Test author model returned type
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Author))
        self.assertEqual(str(data), "onerandomperson")
        self.assertEqual(data.country_of_origin, "shitland")


class ModelpaperusedmaterialTest(TestCase):

    def setUp(self):
        Material.objects.create(material="onerandommat")
        Paper.objects.create()
        self.data1 = PaperUsedMaterial.objects.create(
            material=datetime.date(2022, 5, 24),
            paper="coven1",
            material_used="somethere"
        )

    def test_paperusedmaterial_model_test(self):
        '''
        Test paperusedmaterial model returned type
        '''
        data = self.data1
        self.assertTrue(isinstance(data, PaperUsedMaterial))
        self.assertEqual(str(data), "2022")
        self.assertEqual(data.year_published, datetime.date(2022, 5, 24))
        self.assertEqual(data.convention_published, "coven1")
        self.assertEqual(data.convention_venue, "somethere")
