class Person():#defining a class

    #properties

    #def initte yazdıklarımızdan python bu propertylere sahip olacağını anlıyor aşağıdaki definingleri yapmamıza gerek yoktu:
    name = ""
    age = 0
    gender = ""
    job = "" #initilazierde bundan bahsetmedik bu yüzden illa tanımlanması gereken bir property değil
    #initilazier method: classtan nesne tanımlandığında başlatılacak metot
    def __init__(self,name, age, gender):#yukarıda yazdığımız property
        self.name = name
        self.age = age
        self.gender = gender
    #self classa ref verir ve tüm fonsiyon tanımlamalarında kullanılır
    def test(self):
        print(f"Hello {self.name}")

kemal = Person("Kemal", 21,"male");
print(kemal.gender)
kemal.test()
#classların propertyleri ve metotları(fonksiyonun classtaki kullanımı) ancak o classa ait bir nesne tanımlanırsa kullanılabilir.
kemal.job = "Software Engineer"
print(kemal.job)

class Dog():
    def __init__(self,age):
        self.age = age
        self.dogHumanAge = self.age*7

    def human_age(self):
        humanAge = (self.age)*7
        print(f"kopek yası {self.age} -> insan yası {humanAge}")
        return humanAge

myDog = Dog(5)
myDogAge = myDog.human_age()
print(myDog.dogHumanAge)
print(type(myDogAge))
print(type(myDog))

