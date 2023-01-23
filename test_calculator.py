import Calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == Calculator.add(2, 2)

    def test_subtraction(self):
        assert 0 == Calculator.subtract(2, 2)

    def test_multiplication(self):
        assert 100 == Calculator.multiplication(10,10)
