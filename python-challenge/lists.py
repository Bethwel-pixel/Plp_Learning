#!/usr/bin/python3
number= [x*x*x for x in range(1,6)]


print(number)
number.remove(1)
print(number)
del number[0]
print(number)


