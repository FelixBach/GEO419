import gdal
import rasterio as rio
import numpy as np
from matplotlib import pyplot as plt


def plot():
    # x = [2, 3, 4]
    # y = [2, 4, 6]
    # plt.plot(x, y)
    # plt.show()

    cube = gdal.Open(r'/home/felix/PycharmProjects/py_scripts_419a/lin_to_db_S1B__IW___A_20180828T171447_VV_NR_Orb_Cal_ML_TF_TC.tif')
    band1 = cube.GetRasterBand(1)
    img1 = band1.ReadAsArray(0, 0, cube.RasterXSize, cube.RasterYSize)
    plt.plot(img1/(8192*2))
    plt.show()

    #  rio.open(r'/home/felix/PycharmProjects/py_scripts_419a/lin_to_db_S1B__IW___A_20180828T171447_VV_NR_Orb_Cal_ML_TF_TC.tif') as src:
        # band_db = src.read(1)
        # ras_meta = src.profile

        # min_perc = 2
        # max_perc = 98
        # lo, hi = np.percentile(band_db, (min_perc, max_perc))
        # res_band_db = (band_db.astype(float) - lo / (hi - lo))
        # res_band_db[res_band_db == np.percentile(band_db, max_perc)] = -99

        # res_band_db = np.maximum(np.minimum(band_db+255, 255), 0).astype(np.float64)

        # ras_meta.update(count=1, dtype=rio.float64, nodata=-99)

        # with rio.open('/home/felix/PycharmProjects/py_scripts_419a/tif_db_4.tif', 'w', **ras_meta) as dst:
            # dst.write(res_band_db, 1)

    # band1 = org_tif.GetRasterBand(1)
    # b1 = band1.ReadAsArray()
    # img = np.dstack(b1)
    # f = plt.figure()
    # plt.imshow(img)
    # plt.show()
    # plt.savefig('/home/felix/PycharmProjects/py_scripts_419a/Tiff.png')


plot()


    # min_percent = 2  # Low percentile
    # max_percent = 98  # High percentile
    # lo, hi = np.percentile(img, (min_percent, max_percent))

    # Apply linear "stretch" - lo goes to 0, and hi goes to 1
    # res_img = (img.astype(float) - lo) / (hi - lo)

    # Multiply by 255, clamp range to [0, 255] and convert to uint8
    # res_img = np.maximum(np.minimum(res_img * 255, 255), 0).astype(np.uint8)

    # Display images before and after linear "stretch":
    # cv2.imshow('img', img)
    # cv2.imshow('res_img', res_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()