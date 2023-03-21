my_list= ['a', 'b', 'c', 'd', 'e']
print(my_list)

my_list.append('f')
print(my_list)

my_list.remove('a')
print(my_list)

my_list.insert(6, 'g')
print(my_list)

my_list.pop()
print(my_list)

# index of out of range print(my_list[12])
print(my_list[3])

print(my_list[-3])

list=[8,2,9,3,7,5,6,4,1,10]
list.sort()

print(list)

my_list.extend(list) # my_list=my_list+list
print(my_list)
