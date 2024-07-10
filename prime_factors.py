class PrimeFactor:
    def of(self, number) -> []:
        prime_factors = []
        if number > 1:
            if number == 4:
                prime_factors.append(2)
                prime_factors.append(2)
            else:
                prime_factors.append(number)
        return prime_factors
