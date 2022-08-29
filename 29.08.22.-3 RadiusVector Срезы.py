class RadiusVector:
    def __init__(self, *args):
        self.coords =[*args]

    def __getitem__(self, item):
        if not isinstance(item, (int, float, slice)):
            raise IndexError ("Incorrect !!!!!!!")
        return tuple(self.coords[item]) if type(item) == slice else self.coords[item]

    def __setitem__(self, key, value):
        if not isinstance(key, (int, float, slice)) :
            raise IndexError ("Incorrect !!!!!!!")
        self.coords[key] = value





# d= RadiusVector(1,2,3,4)
# print(d.coords[:2])
# d[1:3] = 9999,444
# print(d.coords)
v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[6]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5
print(v[0])
