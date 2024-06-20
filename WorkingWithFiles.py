
#Created and overwrite
with open('/Users/kemalozyon/Desktop/myPythonFile.txt','w') as myFile:
    myFile.write("Hello Python")
print("Python File just created")
#test code
with open('/Users/kemalozyon/Desktop/myPythonFile.txt','w') as myFile:
    myFile.write("Hello Python 2")
print("Python File is just changed")
#append
with open('/Users/kemalozyon/Desktop/myPythonFile.txt','a') as myFile:
    myString = input("Enter a thing: ")
    myFile.write(f"\n{myString}")
#read
with open('/Users/kemalozyon/Desktop/myPythonFile.txt','r') as myFile:
    print(myFile.read())

#Dosyayı Silme Komutu
import os

if os.path.exists('/Users/kemalozyon/Desktop/myPythonFile.txt'): # Dosyanın varlığını kontrol ettik
    os.remove('/Users/kemalozyon/Desktop/myPythonFile.txt')
    print("Dosya Silindi!")
else:
    print("Dosya bulunumadı!")
