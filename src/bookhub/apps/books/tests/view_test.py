from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from bookhub.apps.books.models import Category


class CategoryViewSetTestCase(APITestCase):
    def setUp(self):
        self.root_category = Category.add_root(
            name='Training',
            slug='training'
        )
        self.child_category = Category.add_child(
            self=self.root_category,
            name='Programing',
            slug='programing'
        )
        self.private_category = Category.objects.create(
            name='Music',
            slug='music',
            is_public=False,
            depth=0
        )

    def test_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only the root category should be returned
        self.assertEqual(response.data[0]["name"], self.root_category.name)

    def test_retrieve_category(self):
        url = reverse('category-detail', args=[self.child_category.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.child_category.name)

    def test_retrieve_private_category(self):
        url = reverse('category-detail', args=[self.private_category.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
