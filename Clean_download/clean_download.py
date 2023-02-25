import os
import shutil

download_path = 'D:\Descargas'

def get_extensions(path):
    extensions = set()
    for filename in os.listdir(path):
        _, extension_in_file = os.path.splitext(filename)
        extensions.add(extension_in_file)
    return list(extensions)


def is_not_blank(string_check):
    # return False if the string is Empty
    return bool(string_check and not string_check.isspace())


def create_folders(extensions):
    for name_of_folders in extensions:
        if is_not_blank(name_of_folders):
            new_folder_path = os.path.join(download_path, name_of_folders.replace('.', ''))
            os.makedirs(new_folder_path, exist_ok=True)


def have_extension(string):
    # return true if the file have an extension
    _, extension_in_file = os.path.splitext(string)
    return is_not_blank(extension_in_file)


def extract_files_in_folder(folder_path):
    file_w_extension = []
    for filename in os.listdir(download_path):
        if have_extension(filename):
            file_w_extension.append(filename)
    return file_w_extension


def move_file(file_w_extension, extensions_download):
    for file_to_move in file_w_extension:
        _, extension = os.path.splitext(file_to_move)
        src_file = os.path.join(download_path, file_to_move)
        if extension in extensions_download:
            dest_file = os.path.join(download_path, extension[1:], file_to_move)
            shutil.move(src_file, dest_file)
            print(f"{src_file} Moved to {dest_file}")


if __name__ == "__main__":
    extensions_in_download = get_extensions(download_path)
    create_folders(extensions_in_download)
    files_in_folder = extract_files_in_folder(download_path)
    move_file(files_in_folder, extensions_in_download)
