"""Calculate clicks given adjustment"""
import numpy as np


def calc_clicks_mrad(adj: float, mrad_per_click: float) -> int:
    """Calculates the number of clicks.

    Args:
        adj (float): Adjustment required in mrad.
        mrad_per_click (float): mrad adjusted per click.

    Returns:
        int: num clicks.
    """

    return np.floor((adj / mrad_per_click) + 0.5)
