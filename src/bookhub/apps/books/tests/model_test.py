from django.test import TestCase

from bookhub.apps.authors.models import Author
from bookhub.apps.books.models import Category, Book
from bookhub.apps.publishers.models import Publisher
from bookhub.apps.translators.models import Translator


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Music',
            slug='music',
            is_public=True,
            depth=0
        )
        self.root_category = Category.add_root(
            name='Training',
            slug='training'
        )
        self.child_category = Category.add_child(
            self=self.root_category,
            name='Programing',
            slug='programing'
        )
        self.grandchild_category = Category.add_child(
            self=self.child_category,
            name='Django',
            slug='django'
        )

    def test_create_category(self):
        self.assertEqual(self.category.name, 'Music')
        self.assertEqual(self.category.slug, 'music')
        self.assertEqual(self.category.depth, 0)
        self.assertTrue(self.category.is_public)

    def test_full_name(self):
        self.assertEqual(self.child_category.full_name, 'Training > Programing')

    def test_get_ancestors_and_self(self):
        ancestors_and_self = self.grandchild_category.get_ancestors_and_self()

        self.assertEqual(len(ancestors_and_self), 3)
        self.assertIn(self.root_category, ancestors_and_self)
        self.assertIn(self.child_category, ancestors_and_self)
        self.assertIn(self.grandchild_category, ancestors_and_self)

    def test_str(self):
        self.assertEqual(str(self.child_category), 'Training > Programing')


class BookTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Fiction',
            slug='fiction',
            depth=0
        )
        self.translator = Translator.objects.create(
            name='John Doe',
            slug='john-doe'
        )
        self.publisher = Publisher.objects.create(
            name='ABC Publications',
            slug='abc-publication',
            founding_year='2023'
        )
        self.author = Author.objects.create(
            name='Jane Smith',
            slug='jane-smith'
        )

        self.book = Book.objects.create(
            category=self.category,
            name='Sample Book',
            slug='sample-book',
            is_public=True,
            meta_title='Sample Book Title',
            description='This is a sample book description.',
            meta_description='Sample meta description.',
            page_count=200,
            publication_year='2022',
            edition='1st',
            is_discountable=True,
            track_stock=True,
            require_shipping=True,
        )
        self.book.translator.add(self.translator)
        self.book.publisher.add(self.publisher)
        self.book.author.add(self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.name, 'Sample Book')
        self.assertEqual(self.book.category, self.category)
        self.assertTrue(self.book.is_public)

    def test_translator_relationship(self):
        self.assertEqual(self.book.translator.count(), 1)
        self.assertEqual(self.book.translator.first(), self.translator)

    def test_slug_unique(self):
        duplicate_book = Book(
            category=self.category,
            name='Another Book',
            slug='sample-book',
            publication_year='2023',
        )
        with self.assertRaises(ValueError):
            duplicate_book.full_clean()
