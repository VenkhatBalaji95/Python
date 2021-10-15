#!/usr/bin/python3

l = [3,2,4,3,61,2,61,-3,7,-1,0,-1,-2,7]
c = l.copy()

print ("List is {0}\n".format(l))


a = l[0]
for i in l:
  if i > a:
    a = i
print ("Maximum number in a list is {a}\n".format(a=a))


a = l[0]
for i in l:
  if i < a:
    a = i
print ("Minimum number in a list is {a}\n".format(a=a))


mx = max(l[0],l[1])
second_max = min (l[0],l[1])
length = len (l)
for i in range(2,length):
  if l[i] > mx:
    second_max = mx
    mx = l[i]
  elif l[i] > second_max and l[i] != mx:
    second_max = l[i]
print ("Second maximum number in a list is {0}\n".format(second_max))


a = []
for i in l:
  if i not in a:
    a.append(i)
print ("Removed duplicates list {0}\n".format(a))


a = l[::-1]
print ("List reverse is {0}".format(a))


b = []
for i in range (len(l)):
  a = l[0]
  for j in l:
    if j < a:
      a = j
  b.append(a)
  l.remove(a)

print ("Actual list {0}".format(c))
print ("Sorted list {0} - own".format(b))
d = sorted(c)
print ("Sorted list {0} - inbuilt\n".format(d))


l = c.copy()
b = []
for i in range (len(l)):
  a = l[0]
  for j in l:
    if j > a:
      a = j
  b.append(a)
  l.remove(a)

print ("Actual list {0}".format(c))
print ("Reverse list {0} - own".format(b))
d = sorted(c, reverse=True)
print ("Reverse list {0} - inbuilt\n".format(d))
