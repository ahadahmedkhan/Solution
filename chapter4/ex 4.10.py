cubes= [value**3 for value in range(1,11)]
print(cubes)
print("first 3 element of list are : ")
for i in cubes[:3]:
 print(i)
print("\nmiddle 3 element of list are : ")
for j in cubes[4:7]:
 print(j)
print("\nlast 3 element of list are : ")
for k in cubes[-4:-1]:
     print(k)