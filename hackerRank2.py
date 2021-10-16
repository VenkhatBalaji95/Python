if __name__ == '__main__':
    s = input() or "aabbbccde"
    a = []
    b = dict()
    for i in s:
        if i not in a:
            a.append(i)
            c = s.count(i)
            b[i] = c
    a = sorted(b.items(), key=lambda x: x[1], reverse=True)
    print (a)
    for i in a[:3]:
        print (i[0], i[1])
      
#Link: https://www.hackerrank.com/challenges/most-commons/problem
