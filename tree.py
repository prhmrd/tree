import os

depth = 0
def show(path, depth):
    for folders in os.listdir(path):
        print(f"{depth * '  '}├───{folders}")
        sub_path = path + '\\' + folders
        if os.path.isfile(sub_path) == False:
            if len(os.listdir(sub_path)) != 0:
                depth += 1
                show(sub_path, depth)
                depth -= 1

show(input("pls enter your path \n"), depth)
