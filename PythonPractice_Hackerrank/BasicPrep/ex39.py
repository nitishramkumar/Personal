states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

cities = {
    'CA':'SF',
    'MI':'Detroit',
    'FL':'Miami'
}

cities['NY'] = 'New york'
cities['OR'] = 'Portland'

print('*' * 10)
print("Ny state has ",cities['NY'])
print("OR state has ",cities['OR'])
print('*' * 10)

for state,abb in states.items():
    print("%s abbreviated as %s"%(state,abb))

for state,city in cities.items():
    print("{0} is part of {1}".format(state,city))
