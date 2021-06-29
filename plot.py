import gdal
import rasterio as rio
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
import geopandas as gpd


def plot_raseter():
    file = 'C:/Users/Felix/PycharmProjects/419a/GEO419_Testdatensatz/lin_to_db/S1B__IW___A_20180828T171447_VV_NR_Orb_Cal_ML_TF_TC.tif'

    raster = gdal.Open(file)

    raster_arr = raster.GetRasterBand(1).ReadAsArray()

    min_perc = 2
    max_perc = 98
    lo, hi = np.percentile(raster_arr, (min_perc, max_perc))
    res_band_db = (raster_arr.astype(float) - lo / (hi - lo))
    res_band_db[res_band_db == np.percentile(raster_arr, max_perc)] = -99

    res_band_db = np.maximum(np.minimum(raster_arr*255, 255), 0).astype(np.float32)

    plt.figure()
    plt.imshow(res_band_db)
    plt.colorbar()
    plt.show()

    plt.figure()
    plt.imshow(raster_arr, cmap='gray')
    plt.colorbar()
    plt.show()


plot_raseter()


# def plot():
#     file = "C:/Users/Felix/PycharmProjects/419a/GEO419_Testdatensatz/lin_to_db/S1B__IW___A_20180828T171447_VV_NR_Orb_Cal_ML_TF_TC.tif"
#
#     # cube = gdal.Open(r'/home/felix/PycharmProjects/py_scripts_419a/lin_to_db_S1B__IW___A_20180828T171447_VV_NR_Orb_Cal_ML_TF_TC.tif')
#     # band1 = cube.GetRasterBand(1)
#     # img1 = band1.ReadAsArray(0, 0, cube.RasterXSize, cube.RasterYSize)
#     # plt.plot(img1/(8192*2))
#     # plt.show()
#
#     with rio.open(file) as src:
#         band_db = src.read(1)
#         ras_meta = src.profile
#         # plt.imshow(band_db)
#         # plt.show()
#
#         min_perc = 2
#         max_perc = 98
#         lo, hi = np.percentile(band_db, (min_perc, max_perc))
#         res_band_db = (band_db.astype(float) - lo / (hi - lo))
#         res_band_db[res_band_db == np.percentile(band_db, max_perc)] = -99
#
#         res_band_db = np.maximum(np.minimum(band_db*255, 255), 0).astype(np.uint8)
#
#         plt.pcolor(res_band_db)
#         # plt.plot(res_band_db)
#         plt.show()
#
#         # ras_meta.update(count=1, dtype=rio.float64, nodata=-99)
#
#         # plt.pcolor(res_band_db)
#         # plt.show(res_band_db)
#
#         # with rio.open('C:/Users/Felix/PycharmProjects/419a/GEO419_Testdatensatz/lin_to_db/test.tif', 'w', **ras_meta) as dst:
#         #     dst.write(res_band_db, 1)
#
#     # band1 = org_tif.GetRasterBand(1)
#     # b1 = band1.ReadAsArray()
#     # img = np.dstack(b1)
#     # f = plt.figure()
#     # plt.imshow(img)
#     # plt.show()
#     # plt.savefig('/home/felix/PycharmProjects/py_scripts_419a/Tiff.png')
#
#
# # plot()

# def plot_gdal():
#     file = "C:/Users/Felix/PycharmProjects/419a/GEO419_Testdatensatz/lin_to_db/S1B__IW___A_20180828T171447_VV_NR_Orb_Cal_ML_TF_TC.tif"
#     dataset = gdal.Open(file)
#     band1 = dataset.GetRasterBand(1)
#     b1 = band1.ReadAsArray()
#
#     # np.seterr(divide='ignore', invalid='ignore')
#     #
#     # min_percent = 2  # Low percentile
#     # max_percent = 98  # High percentile
#     # lo, hi = np.percentile(b1, (min_percent, max_percent))
#     #
#     # res_img = (b1.astype(float) - lo) / (hi - lo)
#     #
#     # # Multiply by 255, clamp range to [0, 255] and convert to uint8
#     # res_img = np.maximum(np.minimum(res_img * 255, 255), 0).astype(np.float)
#
#     # img = np.dstack(b1)
#
#     f = plt.figure()
#     plt.pcolor(b1)
#     # plt.imshow(b1)
#     # plt.imshow(res_img)
#     # plt.savefig('Tiff.png')
#     plt.show()
#
#
# plot_gdal()