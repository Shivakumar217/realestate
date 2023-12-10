from django.test import TestCase

from django.test import TestCase
from .models import Property

class PropertyModelTest(TestCase):
    def setUp(self):
        # Create a sample Property instance for testing
        self.property = Property.objects.create(
            zpid='12345',
            address='123 Main St',
            description='A beautiful house'
        )

    def test_property_creation(self):
        """
        Test that a Property instance is created correctly.
        """
        self.assertEqual(self.property.zpid, '12345')
        self.assertEqual(self.property.address, '123 Main St')
        self.assertEqual(self.property.description, 'A beautiful house')

    def test_property_str_representation(self):
        """
        Test the __str__ method of the Property model.
        """
        expected_str = '123 Main St - 12345'
        self.assertEqual(str(self.property), expected_str)

    def test_unique_zpid_constraint(self):
        """
        Test that the zpid field has a unique constraint.
        """
        with self.assertRaises(Exception) as context:
            # Attempt to create another Property with the same zpid
            Property.objects.create(
                zpid='12345',
                address='456 Oak St',
                description='Another house'
            )

        # Check if the expected IntegrityError was raised
        self.assertIn('UNIQUE constraint failed', str(context.exception))

    def test_default_description_value(self):
        """
        Test that the description field has a default value.
        """
        property_without_description = Property.objects.create(
            zpid='67890',
            address='789 Pine St'
        )

        self.assertEqual(property_without_description.description, '')

    # Add more test cases as needed
