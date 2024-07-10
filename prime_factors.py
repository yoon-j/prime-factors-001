class PrimeFactor:
    def of(self, number) -> []:
        prime_factors = []
        if number > 1:
            if number == 4:
                while not number % 2:
                    prime_factors.append(2)
                    number //= 2

            elif number == 6:
                prime_factors.append(2)
                prime_factors.append(3)
            else:
                prime_factors.append(number)
        return prime_factors
