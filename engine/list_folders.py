import os

def list_folders(folder_path):
    folder_names = []
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            folder_names.append(entry.name)
    return folder_names