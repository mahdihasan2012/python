#recursion
'''
def refun():
    print("Mahdi")
    refun()

refun()


#zip function
list1=["mahdi","mahreen","wasiul"]
list2=["roblox","minecraft","bedwars"]
print(list(zip(list1,list2,)))


#debugging
i=0
while i<10:
    print(i)
i = i + 1
'''

 # #lambda
 # x=lambda a,b: a + b
 # print(x(20,30))


# arrays
# MyArray=["mahdi","wasif","ahiyan"]
# MyArray[1] = "robin"
# print(MyArray)


#classes and objects
# class Mahdi:
#      name = ""
#      number = ""
#
# x= Mahdi()
#
# x.name = "Mahdi"
# x.number = 15
# print(x.name)
#
# x = Mahdi()
# y = Mahdi()
# z = Mahdi()
#
# x.name = "Mahdi"
# y.name = "Wasif"
# z.number = 100000
#
#
# print(x.name)
# print(y.name)
# print(z.number)



#inheritance
# class baba:
#       car = "BMW"
#       tk = "100 crore"
#       house = "7 floor"
#
# class Son1(baba):
#       Smartphone = "IPhone 14 pro max"
#       Smart_TV ="lg oled tv"
#       AC  = "Walton"
#
#
# class Son2(Son1):
#  Laptop = "ASUS"
#  Headphone = "Havit"
#  Computer = "HP"
#
# class Son3(Son2):
#       brokenphone = ""
#       brokenhome = ""
#
# k = Son3()
# print(k.Computer,)


#iterator

# list = [1,2,3,4,5,"Mahdi","Wasif","Robin","Rafin"]
#
#
# for i in list:
#       print(i)
#
# x= iter(list)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# #scope
# a = 50           #global scope
# b = 100
#
#
# def Mahdi():   #local scope
#       global x
#       x = 100
#       print(x)
#
# Mahdi()





#dates
#
# import datetime
# a= datetime.datetime.now()
#
# print(a.strftime("%Y"))



#Math
# print(min(10,20,30,40,50,60))
# print(max(10,48,12,499))
#
#
# print(abs(-2134))
#
# print(pow(5,10))
#


#regex
# import re
#
# text = "The rain in Spain"
# pattern = "[a-h]"
# x = re.findall(pattern , text)
# print(x)


#
# import re
#
# text = " is the special characters"
# pattern = "^1"
# x = re.findall(pattern , text)
# print(x)
# if x:
#       print("yes!! 1 is a special character")
# else:
#       print("Nope! 1 is not a special character")




# #try and except
# try:
#     print("give me output")
# except:
#        print(x)
# print("heloo")
# print("heloo")


#file
# ReadText= open("text.text","r")
# print(ReadText.read())


#delete file
# import os
# os.remove("text.text")

#write file
x = open("mahdi.html", "w")
x.write("<h1> hello world <h1>")

y = open("mahdi.text", "w")
y.write("pls subscribe")
















































































































































