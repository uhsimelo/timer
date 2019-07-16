from os import listdir, chdir, curdir, mkdir
from os.path import exists, abspath
from os import system

def createpath_ifnotexist(path):
    if not exists(abspath(path)):
        folders = path.split("/")[1:]
        folder = folders[0]
        if folder:
            system(f"mkdir {folder}")
        chdir(folder)
        createpath_ifnotexist("./" + '/'.join(folders[1:]))
        chdir("..")
    else:
        return
    
def get_names(path):
    if not exists(abspath(path)):
        createpath_ifnotexist(path)
        return []
    else:
        names = [
            name.split('.')[0]\
            for name in listdir(path)\
                if name.endswith(".json") and name.split('.')[0]\
            ]
        return names

