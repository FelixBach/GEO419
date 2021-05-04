import os
import download
import unzip
import processing_img
from datetime import datetime

start_time = datetime.now()


def main():
    url = 'https://upload.uni-jena.de/data/605dfe08b61aa9.92877595/GEO419_Testdatensatz.zip'

    # no user changes beyond this point

    zip_name = url.rsplit('/', 1)[-1]  # get name after last slash
    folder_name = url.rsplit('.', 2)[1]  # create folder name
    if '/' in folder_name:
        folder_name = folder_name.rsplit('/', 1)[-1]  # remove everything after point
    wd_path = os.getcwd()  # path from current working dir
    path = os.path.join(wd_path, folder_name)  # create folder for unzipping
    print(path)

    download.download(url, zip_name)
    unzip.unzip(path, zip_name)
    processing_img.open_raster_file(path)

    end_time = datetime.now()
    print(f"\n end-time =", end_time - start_time, "Hr:min:sec \n")


# main func
if __name__ == '__main__':
    main()
