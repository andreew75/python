# Костромин Андрей Львович


import os

rootdir = r"/Volumes/Work/Python522/Work"


def process_files(root_dir=rootdir):

    empty_files_dir = os.path.join(root_dir, "empty_files")
    os.makedirs(empty_files_dir, exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_size = os.path.getsize(filepath)

            if file_size > 0:
                relative_path = os.path.join(root_dir, os.path.relpath(filepath, root_dir))
                print(f"'{relative_path}' - {file_size} bytes")
            else:
                new_filepath = os.path.join(empty_files_dir, filename)
                relative_old_path = os.path.join(root_dir, os.path.relpath(filepath, root_dir))

                try:
                    os.replace(filepath, new_filepath)
                except AttributeError:
                    os.rename(filepath, new_filepath)

                relative_new_path = os.path.join(root_dir, os.path.relpath(new_filepath, root_dir))
                print(f"Перемещены пустые файлы: {filename} из '{relative_old_path}' в '{relative_new_path}'")


process_files()
