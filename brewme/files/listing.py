from os import listdir
from os.path import isfile, join

class Listing(object):

    """Docstring for Listing. """

    def __init__(self):
        pass

    def list_files_in_folder(self, path):
        dir_list = listdir(path)
        files = [join(path, file) for file in dir_list if isfile(join(path, file))]
        return files
