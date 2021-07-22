from datetime import datetime

import os
from scripts import download
from scripts import unzip
from scripts import processing_img
from scripts import plot

start_time = datetime.now()


def main():
    url = 'https://upload.uni-jena.de/data/60e5d639dd52a0.78161215/GEO419_Testdatensatz.zip'

    print(f'Type or copy the path to working directory')
    # path = input()
    path = "/home/felix/Dokumente"
    # path = os.getcwd()
    print(path)

    print(f'Type or copy the URL. Make sure that the URL ends on ".zip". Otherwise its can not be downloaded or unziped')
    # url = input()

    download.download(url, path)
    unzip.unzip(url, path)
    processing_img.open_raster_file(url, path)
    plot.plot(path)

    end_time = datetime.now()
    print(f"\n end-time =", end_time - start_time, "Hr:min:sec \n")


# main func
if __name__ == '__main__':
    main()
