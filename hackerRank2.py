from collections import Counter

a = Counter(input() or "aaztrgvvcc").most_common()
b = sorted(a,key = lambda x:(-x[1],x[0]))[:3]
for i,j in b:
    print (i,j)
    
#Link: https://www.hackerrank.com/challenges/most-commons/problem
#Counter link: https://docs.python.org/3/library/collections.html#collections.Counter
#Sorted example link: https://docs.python.org/3/howto/sorting.html
