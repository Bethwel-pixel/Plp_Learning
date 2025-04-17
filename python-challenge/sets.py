#!/user/bin/python3

fruit = set()

fruit = {'Mango', 'Orange', 'Pineapple'}

fruit.add('Guavas')


# Using update to add several sets of the data

greens={'Green', 'Cabbage', 'Spinach', 'Sukuma Wiki'}

fruit.update(greens)

# Using Sum()
print ('Length=', len(fruit))

# Printing all the fruits in the basket
print('initial set:',fruit)

# Getting the max and min

print(f"min={min(fruit)} - max={max(fruit)}")

#set for sum
number={10,20,30}
print (f"Sum of number={sum(number)}")

# Union of Sets
a={'a','b', 'c'}
b= {'c','d','e'}

print(f"A | B is {a.union(b)}")

# Intersection
print(f"A&B is {a.intersection(b)}")

# using the diffference

print(f"A-B is {a.difference(b)}")

# Symetric difference
print(f"a ^ b is {a.symmetric_difference(b)}")

# checking if the sets exist
print(a==b)