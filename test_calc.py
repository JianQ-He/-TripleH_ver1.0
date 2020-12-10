import pytest
from Homework import calculator
from Homework.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 8), (100, 100, 200), (1, 1, 2)], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert self.calc.add(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(3, 5, -2), (100, 100, 0), (1, 1, 0)], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert self.calc.sub(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 15), (100, 100, 10000), (1, 1, 1)], ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(16, 2, 8), (100, 100, 1), (1, 1, 1)], ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        assert self.calc.div(a, b) == expect
