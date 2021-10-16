def merge_the_tools(string, k):
    lis = []
    for i in range(0, len(string), k):
        lis.append(string[i:i+k])
    for i in range (0,len(lis)):
        a = []
        for j in lis[i]:
            if j not in a:
                a.append(j)
        print ("".join(a))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#Input--> AABCAAADA,3
#Link --> https://www.hackerrank.com/challenges/merge-the-tools/problem
