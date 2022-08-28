class Track:

    def __init__(self, start_x, start_y):
        self.start_x, self.start_y = start_x, start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([(x,y),speed])

    def __getitem__(self, num):
        if not isinstance(num, int) or num>=len(self.points):
            raise IndexError('некорректный индекс')
        return self.points[num]

    def __setitem__(self, num, speed):
        if not isinstance(num, int) or num>=len(self.points):
            raise IndexError('некорректный индекс')
        self.points[num][1] = speed
    def coord(self, indx):
        if not isinstance(indx, int) or indx>=len(self.points):
            raise IndexError('некорректный индекс')
        return self.__getitem__(indx)[0]
    def speed(self, indx):
        if not isinstance(indx, int) or indx>=len(self.points):
            raise IndexError('некорректный индекс')
        return self.__getitem__(indx)[1]

tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0

c, s = tr[0]
print(c, s)

tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2
print(tr.points)

tr[2] = 60
print(tr.points)
print(tr.coord(1))
print(tr.speed(2))
c, s = tr[0]
print(c, s)

# res = tr[3] # IndexError
