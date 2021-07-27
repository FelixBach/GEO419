import os
import requests


def download(url, path):
    """This function is used to download a file from a URL

    :param url: string: Is the URL from which the download should be executed
    :param path: string: Is the path where the download file and other folders are created and the result is saved
    :return: Function has no return value
    """
    zip_url = url.rsplit('.', 1)[-1]
    av = requests.head(url).status_code

    if av == 200 and zip_url == 'zip':
        print(f'URL is valid.')

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

    else:
        print(f'URL is not valid. \n')
        while av != 200 or zip_url != "zip":
            print(f'You can type URL or q to stop the download.')
            url = input()
            if url == "q":
                print(f'Download stopped.')
                break
            elif url[:4] == "http":
                zip_url = url.rsplit('.', 1)[-1]
                av = requests.head(url).status_code
                if av == 200 and zip_url == 'zip':
                    print(f'URL valid. ')

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
            else:
                pass
