class Phone():
    def __init__(self,name,price):
        self.name = name
        self.__price = price #Bu kod sayesinde price değişkenine class dışından erişilememz.

        # price değiştirmek için kod:
    def changePrice(self, price):
        self.__price = price
    def info(self):
        print(f"{self.name} price is {self.__price}")



iPhone = Phone("İphone 14",500)
iPhone.info()
iPhone.changePrice(600)
iPhone.__price = 211 #Price değişkeni class dışından değiştirilemez
iPhone.info()