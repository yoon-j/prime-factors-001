class PrimeFactor:
    def of(self, number, divisor=2) -> []:
        if number < 2: return []

        if number % divisor:
            return self.of(number, divisor + 1)
        else:
            return [divisor] + self.of(number // divisor, divisor)
