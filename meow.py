import os

def show(path):
    for folders in os.listdir(path):
        print(f"├───{folders}")
        sub_path = path + '/' + folders
        if os.listdir(sub_path) is not None:
            show(sub_path)


show(input("pls enter your path \n"))
