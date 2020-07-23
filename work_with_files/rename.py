"""
A python script which perform bulk rename to files in a directory
needs three inputs:
    - the direcotory path
    - the name of the file that we want to use (the name should have
    the form of name_)
    - the extention of the file that we want (e.g. .jpg, .png)
"""

import os
from natsort import natsorted
from tqdm import tqdm

# print("Please place the script to the main folder\nand get the direcory name")
# os.chdir('dataset/uw_images/')
# os.chdir(os.getcwd())
# os.chdir(input("Enter the file path: "))

def main(path, new_name, extension):

    os.chdir(path)
    print("The current working directory is: " + str(path))

    for (i, filename) in enumerate(tqdm(natsorted(os.listdir(path)))):
        # print(filename)
        name = os.rename(src=filename, dst='{}{}{}'.format(new_name, i, extension))
    for name in tqdm(os.listdir()):
        f_name, f_ext = os.path.splitext(name)

        f_title, f_num = f_name.split('_')
        f_num = f_num.zfill(4)
        final_name = '{}{}{}'.format(new_name, f_num, f_ext)

        os.rename(name, final_name)
    print("The rename process has finished!!")



if __name__ == '__main__':
    path = input("Enter the directory path: ")
    new_name = input("Enter the new name: ")
    extension = input("Enter the extension for the file: ")
    main(path, new_name, extension) 
