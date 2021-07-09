import os
import glob
import numpy as np
import rasterio as rio
from rasterio.plot import show
from matplotlib import pyplot as plt
from matplotlib import colors, cm


def plot(path):
    proc_folder = 'processed_img'
    raster_path = os.path.join(path, proc_folder)

    file_list = []
    for i, name in enumerate(glob.glob(raster_path + str('/*.tif'))):
        file_list.append(name)
        file_list = [w.replace('\\', '/') for w in file_list]
        # file_name = file_list[i].rsplit('/', 1)[-1]

    for j, img in enumerate(file_list):
        raster = rio.open(file_list[j])
        fig, ax = plt.subplots()
        ax.set_xlabel('Easting')
        ax.set_ylabel('Northing')
        cmap = plt.get_cmap('gist_gray')
        data = raster.read()
        min_per = np.nanpercentile(data, 2)
        max_per = np.nanpercentile(data, 98)

        fig.colorbar(cm.ScalarMappable(norm=colors.Normalize(vmin=min_per, vmax=max_per), cmap=cmap))
        show(raster, transform=raster.transform, vmin=min_per, vmax=max_per, ax=ax, cmap=cmap, title='Result')

        plt.show()
