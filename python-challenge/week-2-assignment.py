#!/bin/usr/python3

#Creating an empty list

my_list=[]

new_list=[10,20,30,40]

my_list.extend(new_list)

print(my_list)

my_list.insert(2,15)

another_list=[50,60,70]

my_list.extend(another_list)

print(my_list)

del my_list[-1]

my_list = [10, 20, 30]
print(f"{30 if 30 in my_list else None}")

