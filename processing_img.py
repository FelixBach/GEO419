import numpy as np
import rasterio as rio
import glob


def calculation(band_1):
    db_pixel = []
    temp_log = np.log10(band_1) * 10
    temp_log[temp_log == -np.inf] = -99
    temp_log[temp_log == -0] = -1
    db_res = temp_log
    db_pixel.append(db_res)

    return db_pixel


def open_raster_file(path):
    file_list = []
    for i, name in enumerate(glob.glob(path + str('/*.tif'))):
        file_list.append(name)
        file_list = [w.replace('\\', '/') for w in file_list]
        file_name = file_list[i].rsplit('/', 1)[-1]

        for j, file in enumerate(file_list):
            with rio.open(file_list[i]) as src:
                band_1 = src.read(1)

                np.seterr(divide='ignore', invalid='ignore')

                db_pixel = calculation(band_1)

                with rio.open(file_list[j]) as src:
                    ras_data = src.read()
                    ras_meta = src.profile

                # make any necessary changes to raster properties, e.g.:
                ras_meta.update(count=1, dtype=rio.float32, nodata=-99)

                with rio.open(f"{path}\lin_to_db_{file_name}", 'w', **ras_meta) as dst:
                    dst.write(db_pixel[j], 1)
