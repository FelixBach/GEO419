import os
import requests


def download(url, path):
    zip_name = url.rsplit('/', 1)[-1]  # get name after last slash
    zip_path = os.path.join(path, zip_name)

    if not os.path.isfile(zip_path):
        print(f'Downloading file')
        r = requests.get(url, stream=True, allow_redirects=True)
        with open(zip_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

    else:
        print(f'Download file {zip_name} already exists')
