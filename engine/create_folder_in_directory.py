import os

def create_folder_in_directory(directory_path, folder_name):

    new_folder_path = os.path.join(directory_path, folder_name)

    # Create the folder if it does not exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created at {new_folder_path}")
    else:
        print(f"Folder '{folder_name}' already exists at {new_folder_path}")

    return new_folder_path