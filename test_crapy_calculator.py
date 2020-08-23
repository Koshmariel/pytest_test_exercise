import pytest
from crapy_calculator import Calculator
from crapy_calculator import CalcError
from numpy.testing import assert_almost_equal

class TestAdd:
    #test addition
    def test_add(self):
        calculator = Calculator()

        result = calculator.add(2, 3)
        expected_result = 5

        assert result == expected_result

    @pytest.mark.parametrize(
        'a, b, expected_result', [
            (1, 2, 3),
            (0, 0, 0),
            (-2, -1, -3),

        ]
    )
    #test addition with parameters
    def test_add_with_param(self, a, b, expected_result):
        calculator = Calculator()
        assert calculator.add(a, b) == expected_result

    # test addition with bad number
    def test_bad_number(self):
        calculator = Calculator()

        with pytest.raises(CalcError):
            calculator.add(100, 1)

#test subtraction
class TestSubtr:
    @pytest.mark.parametrize(
        'a, b, expected_result', [
            (1, 2, -1),
            (0, 0, 0),
            (-2, -1, -1),

        ]
    )
    def test_subtr_with_param(self, a, b, expected_result):
        calculator = Calculator()
        assert calculator.subtr(a, b) == expected_result

#Just a fucture.I have not figured out where to use it.
def test_fixture(my_fixture):
    assert my_fixture == 42


class TestDivision:
    #test division by 0 message
    def test_capsys(self, capsys):
        calculator = Calculator()
        calculator.divide(2, 0)
        div_zero_message = "div_by_0\n"
        out, err = capsys.readouterr()
        assert div_zero_message == out

    # test division by 0
    def div_zero(self):
        calculator = Calculator()

        result = calculator.divide(1, 0)
        expected_result = None

        assert result == expected_result

    # test division
    @pytest.mark.parametrize(
        'a, b, expected_result', [
            (2, 1, 2),
            (100, 2, 50),
            (1, 3, 0.333333),

        ]
    )
    def test_divide(self, a, b, expected_result):
        calculator = Calculator()
        result = calculator.divide(a, b)
        assert_almost_equal(result, expected_result, 6)

#test multiplication
@pytest.mark.timeout(4)
@pytest.mark.parametrize(
    'a, b, expected_result', [
        (1, 2, 2),
        (100, 2, 200),
        (200, 2, 400),

    ]
)
def test_multiply_with_param(a, b, expected_result):
    calculator = Calculator()
    assert calculator.multiply(a, b) == expected_result


