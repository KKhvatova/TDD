
class Calculator:

    def __init__(self):
        self.types_of_number = (int, float, complex)

    def add_function(self, a, b):
        if isinstance(a, self.types_of_number) and isinstance(b, self.types_of_number):
            return a + b
        else:
            raise ValueError

    def subtract_function(self, a, b):
        if isinstance(a, self.types_of_number) and isinstance(b, self.types_of_number):
            return a - b
        else:
            raise ValueError

    def division_function(self, a, b):
        try:
            return a / b
        except:
            raise ValueError
