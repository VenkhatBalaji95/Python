n = int(input() or 10)
l = list(map(int,input().strip().split()))[:n]
c = int(input() or 6)
z = []
for i in range(0,c):
    a = list(map(int,input().strip().split()))
    if a[0] in l:
        z.append(a[1])
        l.remove(a[0])
print (sum(z))

#Link: https://www.hackerrank.com/challenges/collections-counter/problem
