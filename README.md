# GEO - Processing of Sentinel-1 data
This package is based on a project from the M.Sc Geoinformatics in the module "GEOG 419 - Modullare Programmierung in der FE" from the Friedrich-Schiller-Universität Jena and was developed by Felix Bachmann and Maximilian Nestler.
It contains moduls/algorithms to download, unzip and preprocess Sentinel-1-images (other images based on radar should also work). A more detailed overview is given below:

- User query of the URL to download the zip-file
- Download and unzipping of file in user defined directory
- Processing of the input radar dataset (logarithmic scaling)
- Plots stretched result and saves it as PDF
- Checks if the processed files already exist (zip-file, tif-file, result)
- It is possible to run the package from the command line: ```cd\folder_name\GEO\python main.py```

## Installation 
In case you have git installed you can install the package as follows: 

  ```pip install git+https://github.com/FelixBach/GEO419.git@main```

- If there are problems with the package, please open an [issue](https://github.com/FelixBach/GEO419/issues)
- Please note that on Windows you might have to install GDAL and rasterio manually
- If you have trouble installing rasterio or the needed GDAL package on Windows, download and install the .whl files directly from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/).
