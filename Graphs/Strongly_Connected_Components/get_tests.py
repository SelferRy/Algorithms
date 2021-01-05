# def get_tools_dir():
#     import sys
#     import os
#     path = ("C://Users//SelifanovVV//IPython learning//01 All_structure//"
#             + "Engineer_stuff//Weights_v01//General//Coord_search_short//")
#     __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(path)))
#     if not __location__ in sys.path:
#         sys.path.append(__location__)
#     # print(sys.path


def folder_files(directory):
    from os import listdir
    files = [f for f in listdir(directory)]  # if isfile(join("./RES_to_unicode/", f)) -- to exclude folder-names
    return files


def filter_files(directory, key="input"):
    """ Найти подстроку в строке! """
    filter_f = []
    for str_ in folder_files(directory):
        if str_[:len(key)] == key:
            filter_f.append(str_)
    return filter_f