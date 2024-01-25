class demo():
    def __init__(self,name,age):                #constructor
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)

obj=demo("Anuantony",23)
obj.display()