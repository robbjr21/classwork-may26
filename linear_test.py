import pytest

@pytest.mark.parametrize("Result, expected", [(10), "Good"], [(20), "Wrong"])
def test_linear(Result, expected):
  from linear import linearfunction
  answer = linearfunction(Result)
  expected = "10"
  assert answer == expected
