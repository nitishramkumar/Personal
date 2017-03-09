the_count = [1,2,3,4,5]
fruits = ['apples','oranges','bananas']
changes = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print("This is the count {0}".format(number))

for fruit in fruits:
    print("The fruit is %s"%fruit)

for change in changes:
    print("Change %r"%change)

elements = []
for i in range(1,6):
    print("Adding {0} in list".format(i))
    elements.append(i)

print(elements)
