import zipfile
import os


def unzip(path, zip_name):
    if os.path.isdir(path):
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(path)
            if not os.path.isfile(path):
                print(f'Unziping data')
    else:
        print(f'Folder with unziped data exists')
