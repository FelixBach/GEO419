import os
import numpy as np
import rasterio as rio
import glob
import numpy
from matplotlib import pyplot as plt, image as mpimg


def calculation(band_1):
    db_pixel = []
    db_res = 10 * numpy.log10(band_1)
    db_pixel.append(db_res)
    # print(np.nanmedian(db_pixel))
    # print(type(db_pixel[0:2]))
    # for k, value in enumerate(db_pixel):
    #     if value.any() <= -50:
    #         db_pixel[k] = -99
    # print(np.nanmin(db_pixel))
    # print(max(db_pixel))

    return db_pixel


def open_raster_file(path):
    file_list = []
    for i, name in enumerate(glob.glob(path + str('/*.tif'))):
        file_list.append(name)
        file_list = [w.replace('\\', '/') for w in file_list]
        file_name = file_list[i].rsplit('/', 1)[-1]
        print(file_list)
        print(file_name)

        for j, file in enumerate(file_list):
            with rio.open(file_list[i]) as src:
                band_1 = src.read(1)
                print(max(band_1))

                np.seterr(divide='ignore', invalid='ignore')

                db_pixel = calculation(band_1)

                with rio.open(file_list[j]) as src:
                    ras_data = src.read()
                    ras_meta = src.profile

                # make any necessary changes to raster properties, e.g.:
                ras_meta.update(count=1, dtype=rio.float32, nodata=-99)

                with rio.open(file_name, 'w', **ras_meta) as dst:
                    dst.write(db_pixel[j], 1)


