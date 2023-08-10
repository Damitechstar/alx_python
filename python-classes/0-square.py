class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def calculate_area(self):
        return self.__size ** 2

    def calculate_perimeter(self):
        return 4 * self.__size