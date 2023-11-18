import os

def sort_file_names(folder_location):

  file_names = os.listdir(folder_location)

  file_names.sort()

  return file_names

