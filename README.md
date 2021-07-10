# GEOG 419 - Processing of Sentinel-1 data
This package is based on a project in the module "GEOG 419 - Modullare Programmierung in der FE" from the Friedrich-Schiller-Universität Jena and was developed by Felix Bachmann and Maximilian Nestler.
It contains moduls/algorithms to download, unzip and preprocess Sentinel-1-images (other images based on radar should also work). A more detailed overview is given below:

- User query of the URL to download the zip-file
- Download and unzipping of file in **user defined or automatically generated** directory
- Processing of the input radar dataset (logarithmic scaling, other changes if necessary, e.g. delete NoData values)
- Plots the result, saves it as PDF in the directory
- Checks if the processed files already exist (zip-file, tif-file, result)