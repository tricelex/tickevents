from django.test import TestCase


# Create your tests here.
def app(x, y):
    return x + y


class PagesTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(app(3, 8), 11)
