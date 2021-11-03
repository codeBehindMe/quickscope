"""Test the mrad based outputs"""

from src.calculators.mrad import calculate_mrad_approx
import numpy as np


class TestCalculateMradApprox:
    def test_100m(self):
        """
        Test returned result at 100m
        """

        range_mm = 100000
        subtension_mm = 10
        want = 0.1

        got = calculate_mrad_approx(range_mm=range_mm, subtension_mm=subtension_mm)

        assert np.isclose(got, want), f"got {got}, want {want}"
