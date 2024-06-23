#global
myString = "kemal"
def function1():
    #Enclosing
    myString = "ahmet"
    print(myString)

    def newFunction():
        #Local
        myString ="mehmet"
        print(myString)
    newFunction()

function1()
 #B -> builtin: pythonun kendine ait fonksiyonları