"""Calculate mrad based outputs"""

import numpy as np


def calculate_mrad_approx(range_mm: int, subtension_mm: int) -> float:
    """Calculates the milliradian angle.

    Args:
        range_mm (int): Range in mm.
        subtension_mm (int): Subtension in mm.

    Returns:
        float: Miliradian angle.
    """

    return np.arctan(subtension_mm / range_mm) * 1000
