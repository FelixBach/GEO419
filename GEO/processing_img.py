import numpy as np
import rasterio as rio
import glob
import os


def calculation(band_1):
    """This function is used to convert linear values in dB values

    :param band_1: numpy.ndarray: is the first channel from the tif
    :return: list: Returns a list with the new converted dB values
    """
    db_pixel = []
    temp_log = np.log10(band_1) * 10
    temp_log[temp_log == -np.inf] = 'NaN'
    temp_log[temp_log == -0] = -1
    db_res = temp_log
    db_pixel.append(db_res)

    return db_pixel


def process_raster(url, path):
    """This function is used to process the unziped data

    :param url: string: Is the URL from which the download should be executed
    :param path: string: Is the path where the download file and other folders are created and the result is saved
    :return: Function has no return value
    """
    zip_name = url.rsplit('/', 1)[-1]  # get name after last slash
    unzip_folder = zip_name.split('.')[0]
    raster_path = os.path.join(path, unzip_folder)

    file_list = []
    for i, name in enumerate(glob.glob(raster_path + str('/*.tif'))):
        file_list.append(name)
        file_list = [w.replace('\\', '/') for w in file_list]
        file_name = file_list[i].rsplit('/', 1)[-1]

        for j, file in enumerate(file_list):
            with rio.open(file_list[i]) as src:
                band_1 = src.read(1)
                band_1 = np.array(band_1)

                np.seterr(divide='ignore', invalid='ignore')

                db_pixel = calculation(band_1)

                with rio.open(file_list[j]) as src:
                    ras_meta = src.profile

                # make any necessary changes to raster properties, e.g.:
                ras_meta.update(count=1, dtype=rio.float32, nodata=-99)

                out_folder = 'processed_img'
                out_folder_path = os.path.join(path, out_folder)

                if not os.path.isdir(out_folder_path):
                    print(f'Start processing')
                    os.makedirs(out_folder_path)
                else:
                    print(f'Output folder exists')

                img_out_name = os.path.join(out_folder_path, str('lin_to_db_' + file_name))

                if not os.path.isfile(img_out_name):
                    with rio.open(img_out_name, 'w', **ras_meta) as dst:
                        dst.write(db_pixel[j], 1)
                    print(f'Exporting Image')
                else:
                    print(f'Processed Image exists')
