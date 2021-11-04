"""Converts from other units to millimeters"""


class Millimeters:
    @staticmethod
    def from_meters(v: float) -> float:
        return v * 1000

    @staticmethod
    def from_centimeters(v: float) -> float:
        return v * 10

    @staticmethod
    def from_millimeters(v: float) -> float:
        return v
