"""Using higher class functions
This scripts organising files in to images, docs and other. Then sorts in to months.
"""

import os
from datetime import datetime
import shutil

def create_folder_move(folder):

    def func(new_path, src, month, year):
        if not os.path.exists(os.path.join(new_path, f"{folder}/{month} {year}")):
            os.makedirs(os.path.join(new_path, f"{folder}/{month} {year}"))
        try:
            shutil.move(src, (os.path.join(new_path, f"{folder}/{month} {year}")))
        except Exception as e:
            print(e)


    return func

def organise_files(old_path, new_path):

    os.chdir(old_path)
    list_files = os.listdir(old_path)

    for file in list_files:
        src = os.path.join(old_path, file)
        _, file_type = (os.path.splitext(file))
        try:
            time = os.stat(file).st_mtime
            month = datetime.fromtimestamp(time).month
            year = datetime.fromtimestamp(time).year
        except (FileNotFoundError, PermissionError) as e:
            print(e)
        else:
            if file_type == ".jpg":
                images = create_folder_move("images")
                images(new_path, src, month, year)
            elif file_type == ".doc" or file_type == ".pdf":
                docs = create_folder_move("documents")
                docs(new_path, src, month, year)
            else:
                other = create_folder_move("other")
                other(new_path, src, month, year)

organise_files('C:/Users/sam_m/downloads', 'C:/Downloaded files')