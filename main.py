import download_entpacken
import processing_img
from datetime import datetime

start_time = datetime.now()


def main():
    url = 'https://upload.uni-jena.de/data/605dfe08b61aa9.92877595/GEO419_Testdatensatz.zip'
    path = '/home/felix/PycharmProjects/py_scripts_419a/Daten.zip'

    # download_entpacken.download(url, path, chunk_size=128)

    processing_img.open_raster_file(path)

    end_time = datetime.now()
    print(f"\n end-time =", end_time - start_time, "Hr:min:sec \n")
    #
    #

# main func
if __name__ == '__main__':
    main()
