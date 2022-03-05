from django.test import TestCase
import os
from store.logic import operations
import time


os.environ['DJANGO_SETTINGS_MODULE'] = 'books.settings'


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(3, 13, '+')
        self.assertEqual(16, result)

    def test_minus(self):
        result = operations(3, 13, '-')
        self.assertEqual(-10, result)

    def test_multi(self):
        result = operations(6, 13, '*')

        self.assertEqual(78, result)