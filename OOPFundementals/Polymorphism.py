class Banana():
    def __init__(self,name):
        self.name = name

    def info(self):
        print(f"{self.name} = 150cal")

class Apple():
    def __init__(self,name):
        self.name = name

    def info(self):
        print(f"{self.name} = 100 cal")

banana1 = Banana("banana1")
apple1 = Apple("apple1")

myFruitList = [banana1,apple1]

for fruit in myFruitList:
    fruit.info()