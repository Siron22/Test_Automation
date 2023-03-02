# Sequences: __setitem__, __getitem__, __len__, __bool__


class Building:

    def __init__(self, address, numbers_of_floors=6):
        self.address = address
        self.floors = [None] * numbers_of_floors

    def __getitem__(self, index):
        #print(f"In getitem: {index}")
        return self.floors[index]

    def __setitem__(self, key, value):
        #print(f"In set item {key}")
        self.floors[key] = value

    def __len__(self):
        return len(self.floors)

    # def __bool__(self):
    #     return any(self.floors)

building = Building("Kharkiv", numbers_of_floors=0)
#print(len(building))
if building:
    print("Not empty")
else:
    print("Empty")


print(building[2])
print(building[1])
building[1] = "Globallogic"
print(building[1])






for floor in building:
    print(floor)

print(building[0:3])


class Square:

    def __getitem__(self, index):
        print(f"In getitem: {index}")
        return index * index

s = Square()
print(s[3])