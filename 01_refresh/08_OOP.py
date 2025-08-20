"""1.Super class and sub class"""
class Animal:
    name = ""
    def eat(self):
        print("I am eating...")
        
class Parrot(Animal):
    age = 5 # months
    def display(self):
        print(f"My name is = {self.name} and I am {self.age} months old")
        
obj = Parrot()
obj.name = "Tiya"
obj.display()
obj.eat()

"""1.End"""