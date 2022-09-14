"""
def display(path):
    for folders in path:
        print(├folders)
        if (folders has sub folders):
            path = path+/folders
            display(path)



"""
import os

def display(path):
    for folders in os.listdir(path):
        print(f"├" + folders)
        if os.listdir(f"{path}+/{folders}") is not None:
            path += '/' + folders
            display(path)