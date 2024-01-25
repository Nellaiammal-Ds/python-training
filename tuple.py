                      # tuple
tuple1= ("apple","mango","banana")
print(tuple1)
print(len(tuple1)) # length of the tuple

# negative indexing
print(tuple1[-1])

# range of indexing
tuple1 = ("apple","banana","apple","cherry","mango","orange")
print(tuple1[2:5])
print(tuple1[-4:-1])
# check if item exits
if "apple" in tuple1:
    print("yes,apple is in the tuple1")

#append tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
y.remove("orange")
thistuple= tuple(y)
print(thistuple)

#unpacking tuples
fruit= ("orange","apple","mango")
(orange,red,green)= fruit
print(orange)
print(red)
print(green)
#astriech

fruits=("orange","mango","apple","strawberry","cherry")
(orange,green,*red)= fruits
print(orange)
print(green)
print(red)
#looping tuples
thistuple1=("orange","red","blue")
for x in thistuple1:
 print(x)

 # join tuples
 t1 =("a","b","c")
 t2 =(1,2,3)
 t3 =t1 + t2
 print(t3)





