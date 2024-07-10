class PrimeFactor:
    def of(self, number) -> []:
        prime_factors = []
        divisor = 2
        while number > 1:
            while not number % divisor:
                prime_factors.append(divisor)
                number //= divisor
            divisor += 1

        return prime_factors
