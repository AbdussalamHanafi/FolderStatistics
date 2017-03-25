

class Folder():

    def __init__(self, path, number_of_files=0, total_bytes=0, depth=0, parent=None):
        self.__path = path
        self.__number_of_files = number_of_files
        self.__total_bytes = total_bytes
        self.__depth = depth
        self.parent = parent

    def set_current_bytes(self, bytes):
        parent = self
        while (parent is not None):
            parent.__total_bytes += bytes
            parent = parent.parent

    def set_number_of_files(self, file_number):
        parent = self
        while(parent is not None):
            parent.__number_of_files += file_number
            parent = parent.parent

    def set_depth(self, depth):
        parent = self
        while (parent is not None):
            parent.__depth += depth
            parent = parent.parent

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path

    def __str__(self):
        return "Path: " + str(self.__path) + " Number of Files: " + str(self.__number_of_files) + " Total Bytes: " \
               + str(self.__number_of_files) + " Depth: " + str(self.__depth)

