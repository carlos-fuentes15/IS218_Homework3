# pylint: disable=too-few-public-methods

class Calculations:
    history = []
    @classmethod
    def count(cls) -> int:
        return len(cls.history)
class Calculation:
    def __init__(self, a: float, b: float, operator: str):
        self.a = a
        self.b = b
        self.operator = operator
    def __str__(self) -> str:
        return f"{self.a}{self.operator}{self.b}={self.get_result()}"
    def get_result(self) -> float:
        if self.operator == '+':
            return self.a + self.b
        if self.operator == '-':
            return self.a - self.b
        if self.operator == '*':
            return self.a * self.b
        if self.operator == '/':
            if self.b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return self.a/self.b
        raise ValueError(f"Invalid operator:{self.operator}")
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
