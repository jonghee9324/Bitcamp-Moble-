'''
lsr = [1,2,3,4,5,6]
lss = [1,3,5,4,2]

lsr[2] = "세번째"
lss.sort()
lss.reverse()

print(lsr)
print(lss)
'''

'''
이름 = 0
국어성적 = 1
수학성적 = 2
영어성적 = 3
총합 = 4
평균 = 5

i=0
stu =[]

# 5-2-4-1-3 데이터 입력 순위
while( i < 5 ):
    temp = []
    temp.append(input("이름 : "))   
    temp.append(int(input("국어 : ")))
    temp.append(int(input("수학 : ")))
    temp.append(int(input("영어 : ")))
    total =temp[국어성적] + temp[수학성적] + temp[영어성적]
    temp.append(total) 
    temp.append(total/3)
    stu.append(temp)
    i += 1    
print(stu)

# 순차정렬
for j in range(len(stu)):
    for g in range (j+1, len(stu)):
        if(stu[j][총합] < stu[g][총합]):
            tmp = stu[j]
            stu[j] = stu[g]
            stu[g] = tmp
print(stu)
'''

'''
List = [1,2,3,4,5]
List.append(1,2,3,4,5)
Tuple = (10,9,8,7)
test = {"수학" : 60, "국어" : 10, "사회" : 99}
'''

'''
a = int(input("숫자"))

if a == 100:
    print("입력숫자는 100")
    
elif a > 100 :
    print("입력숫자는 100보다큼")
    
else :
    print("입력숫자는 100보다 작")
'''
