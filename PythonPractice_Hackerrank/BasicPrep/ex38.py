ten_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    new_item = more_stuff.pop()
    stuff.append(new_item)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
