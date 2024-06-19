def kwargs_example(**kwargs):
    dictionay = kwargs
    return dictionay

print(type(kwargs_example(kemal = 19, ismet = 16, zeynep = 6)))
kwargs_example(kemal = 19, ismet = 16, zeynep = 6)


#Bir listedeki tüm elemanları Fonsiyon yardımıyla bölme:

def divide_example(number):
    return number / 2
mylist = [1,2,3,4,5,6]
myNewList = list()
for i in mylist:
    myNewList.append(divide_example(mylist[i-1]))

print(myNewList)

#Yukarıdaki işlem map komutuyla daha rahat yapılabilir:

myNewList2 = list(map(divide_example,mylist))
print(myNewList2)

#String Manipulation:

def user_name(*args):
    name = args
    return name
def string_manipulation(string):
    return str(string).capitalize()

myPersonList = user_name(input("İsim Giriniz: "),input("İsim Giriniz"),input("İsim Giriniz"))
myPersonListEdited = list(map(string_manipulation,myPersonList))
print(myPersonListEdited)

#bir liste içerisinde integer geçiyorsa onu bizim için filtrelemesi

my_list = [1,2,3,4,"asfapk","a",True]

def control_list(argumant):
    if type(argumant) == int:
        return argumant
    else:
        print("Yanlış")

print(list(filter(control_list,my_list)))

#en basit haliyle bir listedeki tüm elemanları 3'e bölüp başka bir listeye kaydetmek

mylist=[1,2,3,4,5,6,7,8,9,10]

mynewlist = list(map(lambda num : num /3 , mylist))
print(mynewlist)
