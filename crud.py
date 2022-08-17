class hcl:
	def __init__ (self, empCode, mail):
		self.empCode = empCode
		self.mail = mail
	def newEmployee(self, empCode, mail):
		obj = hcl(empCode,mail)
		ls.append(obj)
		print ("Added employee code: {0} and email ID: {1}".format(empCode,mail))
	def viewEmployee(self):
		count = 1
		for i in ls:
			print ("Viewing person {0} details...".format(count))
			count += 1
			print ("Employee code: {0}".format(i.empCode))
			print ("Email ID: {0}".format(i.mail))
	def updateEmployee(self,empCode,mail):
		flag = False
		for i in ls:	
			if i.empCode == empCode:
				i.mail = mail
				print ("Updated email id for {1} is: {0}".format(i.mail,i.empCode))
				flag = True
				break
		if not flag:
			print ("Given Empcode '{0}' is not present. Please add it first.".format(empCode))
	def deleteEmployee(self,empCode):
		flag = False
		for i in range(len(ls)):
			if ls[i].empCode == empCode:
				del ls [i]
				print ("Deleted employee {0}.".format(empCode))
				flag = True
				break
		if not flag:
			print ("Empcode {0} is not present.".format(empCode))

ls = []
obj = hcl("123","test@hcl.com")
obj.newEmployee("521001889","venkhatbalaji.kuppu@hcl.com")
obj.newEmployee("521001890","venkhatbalaji@hcl.com")

print ("\n")
	
obj.viewEmployee()

print ("\n")

obj.updateEmployee("521001889","test@hcl.com")
obj.updateEmployee("15","test@hcl.com")

print ("\n")

obj.viewEmployee()

print ("\n")

obj.deleteEmployee("521001889")
obj.deleteEmployee("15")

print ("\n")

obj.viewEmployee()
