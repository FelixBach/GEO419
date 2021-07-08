import gdal
import rasterio as rio
from rasterio.plot import show
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
import geopandas as gpd
import rioxarray as rxr
import matplotlib.image as matimg
from PIL import Image
import glob
import os
from mpl_toolkits.basemap import Basemap


def rasterio_plot(path):
    proc_folder = 'processed_img'
    raster_path = os.path.join(path, proc_folder)

    file_list = []
    for i, name in enumerate(glob.glob(raster_path + str('/*.tif'))):
        file_list.append(name)
        file_list = [w.replace('\\', '/') for w in file_list]
        # file_name = file_list[i].rsplit('/', 1)[-1]

    fp = file_list[0]

    img = Image.open(fp)
    arr = np.asarray(img)
    min_per = np.nanpercentile(arr, 2)
    max_per = np.nanpercentile(arr, 98)
    # print(min_per)
    # print(max_per)
    print(f'Printing Image')
    plt.gray()
    plt.imshow(arr, vmin=min_per, vmax=max_per)
    plt.title('Sentinel-1 Szene')
    cb = plt.colorbar()
    cb.set_label('Backscatter in dB')
    plt.show()
