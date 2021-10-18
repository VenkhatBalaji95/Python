n = int(input()) or 3
z = dict()
for i in range(n):
     n, *m = input().split()
     s = list(map(float,m))
     z[n] = s
u = input() or "Harsh"
final = sum(z[u])/len(z[u])
print ("{:.2f}".format(final))
