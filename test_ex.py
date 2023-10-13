import pytest


# Define a fixture to provide the sets of two numbers and their expected results
@pytest.fixture(params=[(3, 2, 1), (5, 7, -2), (10, 5, 5), (0, 0, 0), (-1, -3, 2)])
def number_sets(request):
   return request.param


# Use the @pytest.mark.parametrize decorator to run the test with multiple parameterized values
@pytest.mark.parametrize("number_sets", [(3, 2, 1), (5, 7, -2), (10, 5, 5), (0, 0, 0), (-1, -3, 2) ])
def test_subtraction_with_parametrize(number_sets):
   num1, num2, expected_result = number_sets
   result = num1 - num2
   assert result == expected_result

