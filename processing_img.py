import numpy as np
import rasterio as rio
import glob
import math
from matplotlib import pyplot as plt


def open_raster_file(path):
    file_list = []
    for name in glob.glob(path[:-4] + str('/') + str('*.tif')):
        file_list.append(name)

    with rio.open(file_list[0], 'r') as src:
        ras_meta = src.profile
        arr = src.read()  # read all raster values
        print(arr)
        print('test')
        arr_mean = np.nanmean(arr)
        print(arr_mean)
        arr_db = np.array(arr)
        arr_db = np.array(list(map(np.float, arr)))
        print(arr_db)

    ras_meta.update(count=1,
                    dtype=rio.float32,
                    nodata=0)

    # with rio.open(path[:-4] + str('/') + str('test_result.tif'), 'w', **ras_meta) as dst:
        # dst.write(arr_mean)


    # print(arr.shape)  # this is a 3D numpy array, with dimensions [band, row, col]
    # print(arr)

    # arr_db = 10 * math.log(arr)
    # print(arr_db)

    # return print(np.array(file_list[0]))
