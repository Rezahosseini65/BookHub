from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Profile


# Create your tests here.


class CustomUserTest(TestCase):
    """Test case for custom user model."""

    def test_create_user(self):
        """Test creating a regular user."""
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating a superuser."""
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_profile_on_user_creation(self):
        # Create a user
        user = get_user_model().objects.create(username='testuser')

        # Simulate the user creation signal
        # This will trigger the `create_profile` signal handler
        response = self.client.post('/path/to/user/creation/', {'username': 'testuser'})

        # Check if the user has a profile created
        profile = Profile.objects.filter(user=user).first()
        self.assertIsNotNone(profile)

        # Assert the profile attributes
        self.assertEqual(profile.province, None)
        self.assertEqual(profile.city, None)
        self.assertEqual(profile.address, None)
        self.assertEqual(profile.postal_code, None)
        self.assertEqual(profile.phone, None)