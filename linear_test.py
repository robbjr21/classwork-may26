def test_linear():
  from linear import linearfunction
  answer = linearfunction((0,0),(2,2), 10)
  expected = "10"
  assert answer == expected
  
