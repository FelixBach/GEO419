from datetime import datetime

from GEO import url_path
from GEO import download
from GEO import unzip
from GEO import plot
from GEO import processing_img

start_time = datetime.now()


def main():
    url, path = url_path.url_path()
    download.download(url, path)
    unzip.unzip(url, path)
    processing_img.process_raster(url, path)
    plot.plot(path)

    end_time = datetime.now()
    print(f"\n end-time =", end_time - start_time, "Hr:min:sec \n")


# main func
if __name__ == '__main__':
    main()
