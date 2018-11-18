import unittest
import libpysal
import geopandas as gpd
import numpy as np
from inequality.atkinson import Atkinson


class Atkinson_Tester(unittest.TestCase):

    def test_Atkinson(self):
        s_map = gpd.read_file(libpysal.examples.get_path("sacramentot2.shp"))
        df = s_map[['geometry', 'HISP_', 'TOT_POP']]
        index = Atkinson(df, 'HISP_', 'TOT_POP')
        np.testing.assert_almost_equal(index.statistic, 0.15079259382667654)

if __name__ == '__main__':
    unittest.main()
