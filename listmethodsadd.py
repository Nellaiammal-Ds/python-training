# list - append
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)

# add list to a list
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
# clear
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print(fruits)

# copy
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
print(x)
# count
fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)
# extend
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)
# add a list to the tuple
fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)
print(fruits)
# index()
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)
# insert()
fruits = ['apple', 'banana', 'cherry']

fruits.insert(2, "orange")
print(fruits)
# pop()
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)
print(fruits)
# remove()
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")
print(fruits)
# reverse()
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits)
# sort ()
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)

