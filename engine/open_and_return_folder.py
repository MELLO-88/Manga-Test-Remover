import tkinter as tk
from tkinter import filedialog


def open_and_return_folder():

  root = tk.Tk()
  root.withdraw()

  # Use askdirectory() to open a folder selection dialog
  selected_folder = filedialog.askdirectory(title="Select Folder")

  # Print the selected folder path
  print(f"Selected folder: {selected_folder}")

  # Return the selected folder path
  return selected_folder
