"""
def display(path):
    for x in path:
        print(├x)
        if (x has sub folders):
            display(path+x)



"""
import os

def display(path):
    for folders in os.listdir(path):
        print(f"├" + x)
        if ()