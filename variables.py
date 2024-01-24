      #  Python variables

a= int(input("enter the first value"))
b= int(input("enter the second value"))
print(a+b)

#sample program for variable
x = 5
y = "Antony"
print(x)
print(y)

# casting
x=int(3)
y=float(34)
print(x)
print(y)

# we can get a datatype by using type() function
print(type(x))
print(type(y))

      # variable names

# legal variable
my_var = "Antony"
_my_var = "louis"
myVar = "Raj"
MYVAR = "antu"
myvar2 = "Anu"
print(my_var)
print(_my_var)

  # Assign multiple values
#multiple values for multiple variables

x, y, z = "red", "Blue", "green"
print(x)
print(y)
print(z)

#one value for multiple variables
x=y=z="orange"
print(x)
print(y)
print(z)
#output variables
x="datsirpi is a startup company"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)



       #Strings
print("Hai")
print('Hai')
#slicing strings

b = "Hello, World!"
print(b[2:5])
#slice from the start
b = "Hello,guys"
print(b[:4])
# modify strings
a = "Hello, datasirpi"
print(a.upper())  #uppercase
a = "Hello, World!"
print(a.lower())   #lowercase
# remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# replace string
a = "hello, anu"
print(a.replace("h","y"))
# split string
a = "hello, anu!"
b = a.split(",")
print(b)
#concatenate strings
a = "anu"
b = "antony"
c = a+b
print(c)
#add a space between them
c = a+" "+b
print(c)

# format strings
age = 23
txt = "My name is anu,and Iam {}"
print(txt.format(age))












