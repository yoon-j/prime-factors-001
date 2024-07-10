from unittest import TestCase
from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):

    def setUp(self):
        super().setUp()
        self.prime_factor = PrimeFactor()

    def test_create_prime_factor(self):
        self.assertIsNotNone(self.prime_factor)

    def test_prime_factor_of_1(self):
        self.assertEqual(self.prime_factor.of(1), [])

    def test_prime_factor_of_2(self):
        self.assertEqual(self.prime_factor.of(2), [2])
