import subprocess as sp
import json
import csv

cmd = 'aws iam list-users --output json'

process = sp.run(cmd,capture_output=True,shell=True,text=True)

json_fmt = json.loads(process.stdout)

for i in json_fmt['Users']:
	print (i['UserName'],i['CreateDate'])

file = open('iam.csv','w')
write_object = csv.writer(file)
write_object.writerow(['IAM User','Creation Date'])

for j in json_fmt['Users']:
	write_object.writerow([j['UserName'],j['CreateDate']])
