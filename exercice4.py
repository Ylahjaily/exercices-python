from operator import add

class CustomList(list):
    def __add__(self, other):
        return list(map(add, self, other))

list1 = CustomList([1, 2, 3])
list2 = CustomList([4, 5, 6])

print(list1 + list2)
