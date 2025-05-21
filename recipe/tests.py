from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Test Category")
        for i in range(15):  # Create 15 recipes for testing
            Recipe.objects.create(
                title=f"Recipe {i}",
                description="Test description",
                ingredients="Test ingredients",
                instructions="Test instructions",
                category=self.category
            )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')
        self.assertEqual(len(response.context['recipes']), 10)

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/category_detail.html')
        self.assertEqual(response.context['category'], self.category)
        self.assertTrue(len(response.context['recipes']) >= 1)