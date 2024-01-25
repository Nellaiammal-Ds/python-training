class demo1:
    print("welcome")
    d=50
    def person(self,name,age):
        print(name)
        print(age)
        print(self.d)           #we can use self keyword to access the global variable inside the function
obj=demo1()
obj.person("Antony",24)