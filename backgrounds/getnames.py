import os

def get_jpg_files(directory):
    jpg_files = [file for file in os.listdir(directory) if file.lower().endswith('.jpg')]
    return jpg_files

# Specify the directory path
directory_path = '.'

# Get the list of JPG files
jpg_files_list = get_jpg_files(directory_path)

# Print the list to the terminal
print(jpg_files_list)
