import zipfile
import os


def unzip(url, path):
    zip_name = url.rsplit('/', 1)[-1]  # get name after last slash
    # print(zip_name)
    unzip_folder = zip_name.split('.')[0]
    unzip_folder = os.path.join(path, unzip_folder)
    zip_name = os.path.join(path, zip_name)

    try:
        os.mkdir(unzip_folder)
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(unzip_folder)
            if not os.path.isfile(unzip_folder):
                print(f'Unziping data')

    except FileExistsError:
        if FileExistsError:
            if len(os.listdir(unzip_folder)) == 0:
                print("Directory is empty")
                with zipfile.ZipFile(zip_name, 'r') as zip_ref:
                    zip_ref.extractall(unzip_folder)
                    if not os.path.isfile(unzip_folder):
                        print(f'Unziping data')
            else:
                print(f'Folder {unzip_folder} and data already exists')
