import requests
import zipfile


def download(url, path, chunk_size=128):
    r = requests.get(url, stream=True, allow_redirects=True)
    with open(path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

    with zipfile.ZipFile(path, 'r') as zip_ref:
        unzip_path = path[:-4]
        zip_ref.extractall(unzip_path)
