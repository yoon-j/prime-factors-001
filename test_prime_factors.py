from unittest import TestCase
from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_create_prime_factor(self):
        prime_factor = PrimeFactor
        self.assertIsNotNone(prime_factor)
