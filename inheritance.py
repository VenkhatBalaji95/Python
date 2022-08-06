class parentClass:
    def __init__(self,number):
        self.number = number
    def details(self):
        global z
        z = []
        for i in range (1,self.number+1):
            x = list(input("Enter person detail {0}: ".format(i)).split())
            z.append(x)

class secondParentClass:
    def __init__(self,age):
        self.age = age
    def printAge(self):
        print ("Retirement Age: {0}".format(self.age))

class childClass(parentClass, secondParentClass):
    def __init__(self,number,company,age):
        self.company = company
        parentClass.__init__(self, number)
        secondParentClass.__init__(self, age)
    def findCompany(self):
        count = 0
        for i in z:
            if i[1] == self.company:
                count += 1
        if count > 0:
            print ("Total {0} employee count out of {1}: {2}".format(self.company,self.number,count))
        else:
            print ("No employee works in {0} out of {1}".format(self.company,self.number))
        secondParentClass.printAge(self)

a = childClass(2,"hcl",58)
a.details()
a.findCompany()

print ("\n")

b = childClass(3,"fidelity",60)
b.details()
b.findCompany()
