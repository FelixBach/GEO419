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

    if av != 200:
        while av != 200:
            print(f'URL is not valid. Please enter a new one and hit enter. '
                  f'Make sure that the url ends on ".zip" otherwise it can not be unziped.')
            print(f'You can type s in the console/terminal if you do not want to type a new URL.')
            url = input()

            if url == "s":
                print(f'Download aborted.')
                break
            else:
                pass
                # while url != "s":
                #    print(f'Wrong letter.')
                #    url = input()
                #    if url == "s":
                #        break

            av = requests.head(url).status_code
            zip_url = url.rsplit('.', 1)[-1]
            if av == 200 and zip_url == 'zip':
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
                break
