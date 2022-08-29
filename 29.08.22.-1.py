class Array:
    def __init__(self, max_lenth, cell):
        self.max_lenth = max_lenth
        self.cell = cell
        self.arr = [self.cell() for _ in range(max_lenth)]

    def __repr__(self):
        return f'{self.arr}'
        # return " ".join(map(str, self.arr))

    def check(self, num):
        if not isinstance(num, int) or not -(len(self.arr)) <= num < len(self.arr):
            raise IndexError
        return num

    def __getitem__(self, item):
        self.check(item)
        return self.arr[item].value

    def __setitem__(self, key, value):
        self.check(key)
        self.arr[key].value = value

class Integer:
    def __init__(self, start_value=0):
        self.__start_value = start_value

    @property
    def value(self):
        return self.__start_value
    @value.setter
    def value(self, new_meaning):
        if isinstance(new_meaning, int):
            self.__start_value = new_meaning
        else:
            raise ValueError('должно быть целое число')
    def __repr__(self):
        return str(self.__start_value)




ar_int = Array(10, cell=Integer)
print("arr = ", ar_int.arr)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[5] = 10
print(ar_int[5])
print(ar_int.arr)
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[12] = 1 # должно генерироваться исключение IndexError
# v = Integer(77)
# print(v.value)
# v.value=88
# print(v.value)
# print(ar_int.cell)





