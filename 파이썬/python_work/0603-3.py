'''
ls = [1,2,3,4,5]
ls1 = [11,12,13,14,15]
ls2 = [21,22,23,24,25]
Sum = 0

for x in ls:
    Sum += x
print(Sum)

for x in ls1:
    Sum += x
print(Sum)

for x in ls2:
    Sum += x
print(Sum)



def A(List):
    Sum = 0
    for x in List:
        Sum = Sum + x
        print(Sum)

A(ls)
'''
'''
#성적 다 더하기

수학 = [1,2,3,4,5]
국어 = [11,22,33,44,55]
영어 = [21,22,23,24,25]

def A(List):
    Sum = 0
    for i in List:
        Sum += i
    print("총합 {0}".format(Sum))

A(수학)
A(국어)
A(영어)
'''

'''
a = 1
b=2
def add(a,b):
    return a+b, a-b, a*b, a/b

s, d, p, n = add(a,b)
print("{0},{1},{2},{3}".format(s,d,p,n))
'''

def add (*args):
    Sum = 0
    for i in args:
        Sum += i
    print(Sum)


add(1,2,3,4,5,6,7)
        
