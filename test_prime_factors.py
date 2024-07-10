from unittest import TestCase
from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):

    def test_create_prime_factor(self):
        prime_factor = PrimeFactor()
        self.assertIsNotNone(prime_factor)

    def test_prime_factor_of_1(self):
        prime_factor = PrimeFactor()
        self.assertEqual(prime_factor.of(1), [])

    def test_prime_factor_of_2(self):
        prime_factor = PrimeFactor()
        self.assertEqual(prime_factor.of(2), [2])
