def returnVariable():
	def innerFunction (text):
		return text
	return innerFunction("Welcome to HCL")

normal = returnVariable()
print (normal)

print ("\nClosure & Decorator Function example")

def decoratorFunction(msg):
	def innerFunction (text):
		return text+" "+msg()
	return innerFunction

closure = decoratorFunction(returnVariable)
del decoratorFunction
#decoratorFunction(returnVariable)
print (closure("Hi,"))
