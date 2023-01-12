from django.test import TestCase


class TestStringMethods(TestCase):
    def test_length(self):
        self.assertIsNot(len('yatube'), 5)

# Create your tests here.
