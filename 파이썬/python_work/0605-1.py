'''
class A :
    val = 3
    def func(self):
        global val
        val = 5

aa = A()
aaa = A()

aa.func()

print(aa.val)
print(aaa.val)
'''

'''
#예외 처리 기능 1 제대로 입력할 때까지 입력받기 
while True:
    try : 
        score = int(input("성적 : "))
        print (score)
        break
    except:
        print("에러")
'''

List = [ "홍길동", 70, 80, 90, "수", "우"]
Sum = 0
for i in List:
    try:
        Sum += i
    except :
        print("에러지뤙~")
print(Sum)
