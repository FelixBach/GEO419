from datetime import datetime

import os
import download
import unzip
import processing_img
import plot

start_time = datetime.now()

# TODO: kleines readme schreiben für das Skript


def main():
    url = 'https://upload.uni-jena.de/data/60e5d639dd52a0.78161215/GEO419_Testdatensatz.zip'

    print(f'Type or copy the path to working directory')
    # path = input()
    path = os.getcwd()
    # print(path)

    print(f'Type or copy the URL')
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
