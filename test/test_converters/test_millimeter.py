from src.converters.millimeter import Millimeters


class TestMillimeters:
    def test_from_meters(self):

        got = Millimeters.from_meters(1)
        want = 1000

        assert got == want

    def test_from_centimeters(self):

        got = Millimeters.from_centimeters(1)
        want = 10

        assert got == want

    def test_from_millimeters(self):

        got = Millimeters.from_millimeters(1)
        want = 1

        assert got == want
