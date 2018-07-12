from django.test import TestCase

from colours.models import Palette, Colour


class PaletteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Palette.objects.create(name='Red palette')
    
    def setUp(self):
        self.p = Palette.objects.get(id=1)
    
    def test_name_label(self):
        label = self.p._meta.get_field('name').verbose_name
        self.assertEqual(label, 'name')

    def test_name_max_length(self):
        max_length = self.p._meta.get_field('name').max_length
        self.assertEqual(max_length, 128)

    def test_object_name(self):
        name = self.p.name
        self.assertEqual(name, str(self.p))

    def test_slug_label(self):
        label = self.p._meta.get_field('slug').verbose_name
        self.assertEqual(label, 'slug')

    def test_object_slug(self):
        self.assertEqual(self.p.slug, 'red-palette')

    def test_get_object_by_name(self):
        p = Palette.objects.get(name="Red palette")
        self.assertEqual(p, self.p)

    def test_object_absolute_url(self):
        self.assertEqual(self.p.get_absolute_url(), '/colours/palette/red-palette/')

class ColourModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        p = Palette.objects.create(name='Red palette')
        Colour.objects.create(
            palette=p,
            name='Red colour',
            hex_code="#f44336",
            additional_info="Just the colour red."
        )
    
    def setUp(self):
        self.p = Palette.objects.get(name="Red palette")
        self.c = Colour.objects.get(id=1)

    def test_palette_label(self):
        label = self.c._meta.get_field('palette').verbose_name
        self.assertEqual(label, 'palette')

    def test_object_palette(self):
        self.assertEqual(self.p, self.c.palette)

    def test_name_label(self):
        label = self.c._meta.get_field('name').verbose_name
        self.assertEqual(label, 'name')

    def test_name_max_length(self):
        max_length = self.c._meta.get_field('name').max_length
        self.assertEqual(max_length, 128)

    def test_object_name(self):
        name = self.c.name
        self.assertEqual(name, str(self.c))

    def test_hex_code_label(self):
        label = self.c._meta.get_field('hex_code').verbose_name
        self.assertEqual(label, 'hexidecimal code')

    def test_hex_code_max_length(self):
        max_length = self.c._meta.get_field('hex_code').max_length
        self.assertEqual(max_length, 7)

    def test_additional_info_label(self):
        label = self.c._meta.get_field('additional_info').verbose_name
        self.assertEqual(label, 'additional info')

    def test_slug_label(self):
        label = self.c._meta.get_field('slug').verbose_name
        self.assertEqual(label, 'slug')

    def test_object_slug(self):
        self.assertEqual(self.c.slug, 'red-colour')

    #def test_object_absolute_url(self):
    #    self.assertEqual(self.p.get_absolute_url(), '/colours/palette/red-colour')
