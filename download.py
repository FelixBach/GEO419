import os
import requests


def download(url, zip_name):
    if not os.path.isfile(zip_name):
        r = requests.get(url, stream=True, allow_redirects=True)
        with open(zip_name, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
    else:
        print('zip-file exists')
