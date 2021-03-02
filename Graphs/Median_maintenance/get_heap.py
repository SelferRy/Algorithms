def graphs_dir():
    import sys
    import os
    path = os.getcwd().rsplit("\\", 1)[0]  #  "C://prog//projects//Algorithms//"
    # __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(path)))
    if not path in sys.path:
        sys.path.append(path)