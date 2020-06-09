import subprocess 

#to copy the results in the outputpython file.
with open('outputpython.txt','w') as f:
   subprocess.run(['ls','-la'],stdout=f,text=True,check=True)

#to print the results using PIPE method
a = subprocess.run(['ls','-la'],stdout=subprocess.PIPE,text=True,check=True)
print (a.stdout)

file_name='ven.txt'
args='cat '+file_name

#to print the results using capture_output method
b = subprocess.run(args,capture_output=True,text=True,check=True,shell=True)
print (b.stdout)

#to pass the input from the previous step
c = subprocess.run(['grep','-n','v'],capture_output=True,text=True,check=True,input=b.stdout)
print (c.stdout)
