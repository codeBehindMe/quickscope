from src.calculators.clicks import calc_clicks_mrad


class TestCalcClicksMrad:
    def test_fits_correct(self):

        """
        #FIXME: Missing docstring
        """
        adj = 0.1
        click_size = 0.1

        want = 1

        got = calc_clicks_mrad(adj, click_size)

        assert got == want

    def test_almost_click_size(self):
        """
        #FIXME: Missing docstring
        """

        adj = 0.09
        click_size = 0.1

        want = 1

        got = calc_clicks_mrad(adj, click_size)

        assert got == want

    def test_biased_towards_small_side(self):
        """
        #FIXME: Docstring
        """

        adj = 0.04
        click_size = 0.1

        want = 0

        got = calc_clicks_mrad(adj, click_size)

        assert got == want
