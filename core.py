import random, copy
m = 98  #数量
l = 30  #长度
outcome = []
for n in range(0, m):
    a = [0]*l
    c = [0]*l
    for i in range(0,len(a)):
        a[i]=random.random()
    b = copy.deepcopy(a)
    a.sort()
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i]==b[j]:
                c[i]=j + 1
    outcome.append(c)
for i in range(0,len(outcome)):
    print(outcome[i])
