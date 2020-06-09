import subprocess as sp

cmd = 'aws iam list-users --output json'

process = sp.Popen(cmd,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,text=True)

wait = process.wait()

outs, errs = process.communicate()

print (outs)
print (errs)
