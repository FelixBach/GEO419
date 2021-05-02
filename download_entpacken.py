import os
import requests
import zipfile


def download(url):
    zip_name = url[56:]  # name from zip file
    folder_name = url[56:-4]  # folder name for unzipping
    wd_path = os.getcwd()  # path from current working dir
    path = os.path.join(wd_path, folder_name)  # create folder for unzipping

    if not os.path.isfile(zip_name):
        r = requests.get(url, stream=True, allow_redirects=True)
        with open(zip_name, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
    else:
        print('zip-file exists')

    if not os.path.exists(path):
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(path)
    else:
        print('zip folder exists')
