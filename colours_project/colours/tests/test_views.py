from django.test import TestCase
from django.urls import reverse

from colours.models import Palette, Colour


class IndexViewTest(TestCase):
    def test_url_exists_at_desired_location(self):
        res = self.client.get('/colours/')
        self.assertEqual(res.status_code, 200)
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_url_access_by_name(self):
        res = self.client.get(reverse('colours:index'))
        self.assertEqual(res.status_code, 200)

    def test_correct_template_used(self):
        res = self.client.get(reverse('colours:index'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'colours/index.html')

    def test_correct_heading_shown(self):
        res = self.client.get(reverse('colours:index'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "No colours available.")

    def test_correct_num_palettes_shown_1(self):
        for n in range(0, 5):
            Palette.objects.create(name="Palette %s" % n)
        res = self.client.get(reverse('colours:index'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['colour_palettes']), 5)

    def test_correct_num_palettes_shown_2(self):
        for n in range(0, 6):
            Palette.objects.create(name="Palette %s" % n)
        res = self.client.get(reverse('colours:index'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['colour_palettes']), 6)

    def test_correct_num_palettes_shown_3(self):
        for n in range(0, 13):
            Palette.objects.create(name="Palette %s" % n)
        res = self.client.get(reverse('colours:index'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['colour_palettes']), 6)

    def test_active_section_present(self):
        res = self.client.get(reverse('colours:index'))
        self.assertEqual(res.status_code, 200)
        self.assertTrue('active_section' in res.context)
        self.assertEqual(res.context['active_section'], 'colours_index')


class PaletteDetailsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Palette.objects.create(name='Red')

    def setUp(self):
        self.p = Palette.objects.get(id=1)

    def test_url_exists_at_desired_location(self):
        res = self.client.get('/colours/palettes/red/')
        self.assertEqual(res.status_code, 200)

    def test_url_access_by_name(self):
        res = self.client.get(reverse('colours:palette_details', args=[self.p.slug]))
        self.assertEqual(res.status_code, 200)

    def test_url_access_by_object(self):
        res = self.client.get(self.p.get_absolute_url())
        self.assertEqual(res.status_code, 200)

    def test_correct_template_used(self):
        res = self.client.get(self.p.get_absolute_url())
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'colours/palette_details.html')

    def test_correct_heading_shown(self):
        res = self.client.get(self.p.get_absolute_url())
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "No colours available.")

    def test_active_section_present(self):
        res = self.client.get(reverse('colours:palette_details', args=[self.p.slug]))
        self.assertEqual(res.status_code, 200)
        self.assertTrue('active_section' in res.context)
        self.assertEqual(res.context['active_section'], 'colours_palette')


class PaletteListViewTest(TestCase):
    def test_url_exists_at_desired_location(self):
        res = self.client.get('/colours/palettes/')
        self.assertEqual(res.status_code, 200)

    def test_url_access_by_name(self):
        res = self.client.get(reverse('colours:palette_list'))
        self.assertEqual(res.status_code, 200)

    def test_correct_template_used(self):
        res = self.client.get(reverse('colours:palette_list'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'colours/palette_list.html')

    def test_correct_heading_shown(self):
        res = self.client.get(reverse('colours:palette_list'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "No palettes available.")

    def test_palette_pagination_1(self):
        for n in range(0, 7):
            Palette.objects.create(name="Palette %s" % n)
        res = self.client.get(reverse('colours:palette_list'))
        self.assertEqual(res.status_code, 200)
        self.assertTrue('is_paginated' in res.context)
        self.assertTrue(res.context['is_paginated'] == False)
        self.assertTrue(len(res.context['palette_list']) == 7)

    def test_palette_pagination_2(self):
        for n in range(0, 8):
            Palette.objects.create(name="Palette %s" % n)
        res = self.client.get(reverse('colours:palette_list'))
        self.assertEqual(res.status_code, 200)
        self.assertTrue('is_paginated' in res.context)
        self.assertTrue(res.context['is_paginated'] == False)
        self.assertTrue(len(res.context['palette_list']) == 8)

    def test_palette_pagination_3(self):
        for n in range(0, 10):
            Palette.objects.create(name="Palette %s" % n)
        res = self.client.get(reverse('colours:palette_list')+'?page=2')
        self.assertEqual(res.status_code, 200)
        self.assertTrue('is_paginated' in res.context)
        self.assertTrue(res.context['is_paginated'] == True)
        self.assertTrue(len(res.context['palette_list']) == 2)

    def test_active_section_present(self):
        res = self.client.get(reverse('colours:palette_list'))
        self.assertEqual(res.status_code, 200)
        self.assertTrue('active_section' in res.context)
        self.assertEqual(res.context['active_section'], 'colours_palette')
