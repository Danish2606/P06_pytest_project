from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321 
        b = 2000
        cal = Calculator()

        # act
        result =cal.subtract(a,b)

        # assert
        expected = 2321
        assert result == expected 
    
    def test_multiply(self):
        #arrange
        a = 2
        b = 6 
        cal = Calculator()

        #act 
        result = cal.multiply(a,b)

        #assert
        expected = 12
        assert result == expected 

    def test_divide(self):
        #arrange
        a = 6
        b = 2
        cal = Calculator()

        #act 
        result = cal.divide(a,b)


        #assert
        expected = 3
        assert result == expected

        