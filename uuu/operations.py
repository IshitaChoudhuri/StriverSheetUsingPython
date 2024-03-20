firstname = "Ishita"
lastname = "Choudhuri"
print(firstname+" "+lastname)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4]
list.append(8)
print(list)
list.pop(0)  # removes the first element
print(list)
list.pop(-1)
print(list)

fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)

# dictionary
fruits = {"apple": 1, "banana": 2, "cherry": 3}
fruits["apple"] = 4
fruits["banana"] = 6

print(fruits)

del fruits["cherry"]
del fruits["apple"]

print(fruits)
