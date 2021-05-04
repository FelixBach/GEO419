import zipfile
import os


def unzip(path, zip_name):
    if not os.path.exists(path):
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(path)
    else:
        print('zip folder exists')
