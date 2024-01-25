class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")
from modules.my_module import MyClass

        # Create an instance of MyClass
obj = MyClass("Alice")
obj.greet()  # Output: Hello, Alice!
from modules import my_module

# Create an instance of MyClass
        obj = my_module.MyClass("Bob")
        obj.greet()  # Output: Hello, Bob!