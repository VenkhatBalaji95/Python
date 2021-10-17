from itertools import *

a,b = map(int,input().split())
z = []

for i in range(a):
    c = list(map(int,input().split()))[:7]
    z.append(c)
MAX = -1
for i in product(*z):
    MAX = max(sum(map(lambda x: x*x, i))%b,MAX)
print (MAX)

#Link: https://www.hackerrank.com/challenges/maximize-it/problem
