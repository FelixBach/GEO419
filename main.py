from datetime import datetime

import os
from scripts import download
from scripts import unzip
from scripts import processing_img
from scripts import plot

start_time = datetime.now()


def main():
    url = 'https://upload.uni-jena.de/data/60e5d639dd52a0.78161215/GEO419_Testdatensatz.zip'

    print(f'Type or copy the entire path to the working directory')
    print(f'Example path: "C:/folder_name/"')
    path = input()
    # path = "/home/felix/Dokumente"

    if os.path.exists(path):
        print(f'Working directory is valid.')
    else:
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path))
            print(f'Working directory is created')

    # path = os.getcwd()

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
