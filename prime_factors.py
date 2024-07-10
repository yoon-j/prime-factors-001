class PrimeFactor:
    def of(self, number) -> []:
        prime_factors = []
        if number > 1:
            divisor = 2
            if number == 4:
                while not number % divisor:
                    prime_factors.append(divisor)
                    number //= divisor

            elif number == 6:
                while number > 1:
                    while not number % divisor:
                        prime_factors.append(divisor)
                        number //= divisor
                    divisor += 1
            else:
                prime_factors.append(number)
        return prime_factors
