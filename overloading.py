num1 = 4
num2 = 2
print (num1 + num2)

name1 = "Venkhat"
name2 = " Balaji"
print (name1 + name2)

class addition:
    def __init__(self, a):
        self.a = a
   
    def __add__(self, obj):
    	print ("inside addition")
    	#return "Return inputs - {0},{1}".format(self.a,obj.a)
    	return self.a + obj.a

obj1 = addition(4)
obj2 = addition(2)
obj3 = addition("Venkhat")
obj4 = addition(" Balaji")

print(obj1 + obj2)
print(obj3 + obj4)
