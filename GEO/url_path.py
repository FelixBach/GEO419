import os
import requests


def url_path():
    """This function is used to get the URL and a path as String. The user has to type the URL and path via the
    terminal/prompt.

    :parameter: This function has no parameter(s)
    :return: String: url
    :return: String: path
    """
    #url = 'https://upload.uni-jena.de/data/60e5d639dd52a0.78161215/GEO419_Testdatensatz.zip'
    #url = 'https://upload.uni-jena.de/data/69990e5d639dd52a0.78161215/GEO419_Testdatensatz.zip'  # w_url

    special_characters = "!@#$%^&*()-+?_=,<>"

    print(f'First, the path of the working directory must be entered.')
    print(f'Example path (Windows): "C:/folder_name/"')
    print(f'Example path (Linux): /home/user/Documents/ \n')
    print(f'Special Characters like {special_characters} are not allowed in the path name \n')
    print(f'Type or copy the entire path to the working directory in the terminal/prompt. \n')
    #path = input()
    path = "/home/felix/Dokumente/"

    if any(c in special_characters for c in path):
        print(f'Path contains special character(s). Please type or copy a new path \n')
        while any(c in special_characters for c in path):
            path = input()
            if os.path.exists(path):
                print(f'Working directory is valid. \n')
            else:
                if not os.path.exists(path):
                    try:
                        os.makedirs(os.path.dirname(path))
                        print(f'Working directory is created')
                    except FileExistsError:
                        print(f'Working directory already exists.')

    else:
        if os.path.exists(path):
            print(f'Working directory is valid. \n')
        else:
            if not os.path.exists(path):
                try:
                    os.makedirs(os.path.dirname(path))
                    print(f'Working directory is created')
                except FileExistsError:
                    print(f'Working directory already exists.')

    print(f'The second thing to do is to specify the URL.')
    print(f'Type or copy the URL. Make sure that the URL ends on ".zip". Otherwise its can not be downloaded. \n')
    url = input()

    while url[:4] != "http":
        print(f'URL has to start with "http". Please enter a new one or type q to quit.')
        url = input()
        if url == "q":
            break

    zip_url = url.rsplit('.', 1)[-1]
    av = requests.head(url).status_code

    if av == 200 and zip_url == 'zip':
        print(f'URL is valid.')
    else:
        print(f'\n URL is not valid.')
        while av != 200 or zip_url != "zip":
            print(f'You can type a new URL or q to stop the download. \n')
            url = input()
            if url == "q":
                print(f'Download stopped.')
                break
            elif url[:4] == "http":
                zip_url = url.rsplit('.', 1)[-1]
                av = requests.head(url).status_code
                if av == 200 and zip_url == 'zip':
                    print(f'URL valid.')
            else:
                pass

    return url, path
