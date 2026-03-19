"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([1, 2, 3, 4]) == 10
    assert max_subarray_sum([-3, -1, -2]) == -1
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-5]) == -5
    assert max_subarray_sum([0, -1, 2, 0]) == 2
    assert max_subarray_sum([-10, 2, 3, 4, -1, -2, 1, 5, -3]) == 12

if __name__ == "__main__":
    pytest.main()