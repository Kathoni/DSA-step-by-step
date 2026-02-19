areas=[1,2,3]

areas.append(4)
print(areas)

areas.append(5)
print(areas)

areas.append(6)
print(areas)
x = areas[:]
x[1] = 10
print(x)
#slicing a list creates a copy of the list, so modifying x does not affect areas
print(areas[1:4])

y = [[1,2,3],
     ["mom","dad","brother"],
     [7,True,"hello"]]
print(y[0][1])
print(y)
#manipulating a nested list
y[1][1] = "sister"
print(y)