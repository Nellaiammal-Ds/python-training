class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

# _init_ function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)

#  using _str_() fun

class Person1:
  def _init_(self, name, age):
    self.name= name
    self.age = age
    def __str__(self):
      return f"{self.name}({self.age})"
    p3= Person1 ("Antony", 24)
    print(p3)

