import os


def get_path(path_name):
    path = input("Type " + path_name + ": ")
    if path.lower() == "exit":
        quit()
    flag = os.path.isdir(path)
    if flag:
        return path
    else:
        print(":: Path Invalid, Try Again or Type exit to close script")
        get_path(path_name)
