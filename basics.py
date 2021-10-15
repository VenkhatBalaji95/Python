#!/usr/bin/python3

print ("Refer: 1. https://www.programiz.com/python-programming/methods/list/sort \n 2. https://www.datacamp.com/community/tutorials/python-list-function?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9298754&gclid=Cj0KCQjwqp-LBhDQARIsAO0a6aK31ebsQu2NC3u4rjgg5HJAZ-bD80xDy7PUgz2ZLEs6x7zyPDdnUoIaAoNoEALw_wcB \n")
print ("Variable declaration...")
#Int variable declaration. Default value is 0
num = int()
print ("Type is {0}".format(type(num)))
print ("Value is '{0}'\n".format(num))

#Str variable declaration
string = str()
print ("Type is {0}".format(type(string)))
print ("Value is '{0}'\n".format(string))

#List variable declaration
lis = list()
print ("Type is {0}".format(type(lis)))
print ("Value is '{0}'\n".format(lis))

#Getting input from user. Default type is string
strInput = input("Enter the string: ")
print ("Type is {0}".format(type(strInput)))
print ("Value is '{0}'\n".format(strInput))

#Input for int
intInput = int (input ("Enter the number: "))
print ("Type is {0}".format(type(intInput)))
print ("Value is '{0}'\n".format(intInput))

#Input for list
num = int(input("Enter number of elements: "))
listInput = list(map(int,input("Enter ',' seperated numbers : ").split(",")))[:num]
print ("Type is {0}".format(type(listInput)))
print ("Value is '{0}'\n".format(listInput))

print ("List functions...")

#To sort the list. By default it will sort in ascending order
listBackup = listInput
print ("Before sort... Value is {0}".format(listInput))
listInput.sort()
print ("After sort... Value is {0}\n".format(listInput))

#To sort the list and assign the return value to a variable. Default is ascending
newList = sorted(listBackup)
print ("New list value using sorted method is {0}\n".format(newList))

#To reverse the list
print ("Before reverse... Value is {0}".format(listInput))
listInput.reverse()
print ("After reverse... Value is {0}\n".format(listInput))
