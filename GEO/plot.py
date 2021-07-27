import os
import glob
import numpy as np
import rasterio as rio
from rasterio.plot import show
from matplotlib import pyplot as plt
from matplotlib import colors, cm
from matplotlib.ticker import FormatStrFormatter


def plot(path):
    """ This function is used to plot the result.

    :param path: string: Is the path where the download file and other folders are created and the result is saved.
    :return: Function has no return value.
    """
    proc_folder = 'processed_img'
    raster_path = os.path.join(path, proc_folder)

    file_list = []
    for i, name in enumerate(glob.glob(raster_path + str('/*.tif'))):
        file_list.append(name)
        file_list = [w.replace('\\', '/') for w in file_list]
        file_name = file_list[i].rsplit('/', 1)[-1]

    for j, img in enumerate(file_list):
        raster = rio.open(file_list[j])
        data = raster.read()

        min_per = np.nanpercentile(data, 2)
        max_per = np.nanpercentile(data, 98)

        fig, ax = plt.subplots(figsize=(10, 8))

        title = file_list[j].rsplit('/', 1)[-1]
        title = title[:-4]

        cmap = plt.get_cmap('gist_gray')

        colb = plt.colorbar(cm.ScalarMappable(norm=colors.Normalize(vmin=min_per, vmax=max_per), cmap=cmap))

        ax.set_xlabel('Easting')
        ax.set_ylabel('Northing')
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
        colb.set_label('Backscatter in dB')

        show(raster, transform=raster.transform, vmin=min_per, vmax=max_per, ax=ax, cmap=cmap, title=title)
        plt.tight_layout()
        plt.savefig(f'{path}/{title}.pdf', bbox_inches='tight')
        plt.show()

    file_list.clear()
