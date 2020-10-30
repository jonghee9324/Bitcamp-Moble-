'''
class student:
    name=""
    address=""
    age=0
    score=0
    rank=0
    def __init__(self, n, ad, ag, s):
        self.name = n
        self.address = ad
        self.age = ag
        self.score = s
    def set_rank(self, r):
        self.rank = r
    


stu  = student("asdf", "123", 20, 55)

print(stu.name)

'''
'''

class Rect:
    count =0
    def __init__(self, wid, hei):
        self.wid = wid
        self.hei = hei
        Rect.count +=1
    def calc(self):
        area = self.wid * self.hei
        return area


class C(Rect):
    count = 40
    
'''
class A() :
    a=1

class B():
    a=81
class C(A,B)
    pass

mC = C()
print(mC.a)



