import os
from tqdm import tqdm


def main(path, new_name, extension):

    os.chdir(path)
    try:
        for i, filename in enumerate(os.listdir(path)):
            name = os.rename(src=filename, dst=f'{new_name}{i}{extension}')
        for name in tqdm(os.listdir()):
            f_name, f_ext = os.path.splitext(name)
            f_num = f_name.split('.')
            final_name = f'{new_name}{f_num}{f_ext}'
            
            os.rename(name, final_name)
            print("The rename process has finished.")
    except:
        print("The name already exists")


if __name__ == '__main__':
    path = os.path.normpath('D:\\giann\\Documents\\Machine_learning\\PhD_project\\Dataset\\cleanning\\')
    new_name = input("Enter the new name: ")
    extension = input("Enter the extension for the file: ")
    main(path, new_name, extension)
