# create a function that read files from a directory and rename them with a list of names

import os

def rename_files():
    # read names from nombres.txt
    with open('nombres.txt', 'r') as f:
        new_names = [line.strip() for line in f]

    file_list = os.listdir(r"C:\Users\Jose Luis Barboza\Desktop\Rename\archivos")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(r"C:\Users\Jose Luis Barboza\Desktop\Rename\archivos")

    # make sure there are enough new names for all files
    if len(file_list) != len(new_names):
        print("Error: El número de nombres no es igual al número de archivos.")
        return

    for file_name, new_name in zip(file_list, new_names):
        print("Old Name - " + file_name)
        # get the file extension
        extension = os.path.splitext(file_name)[1]
        # append the extension to the new name
        new_name_with_extension = new_name + extension
        print("New Name - " + new_name_with_extension)
        try:
            os.rename(file_name, new_name_with_extension)
        except Exception as e:
            print(f"Error renaming file {file_name}: {e}")

    os.chdir(saved_path)

rename_files()