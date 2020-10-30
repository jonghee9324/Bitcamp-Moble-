#실습 1
'''
i = 1
total = 0
while i <= 1000:
    if i%3 == 0:
        total += i
    i += 1

print(total)

'''
'''
#실습3(별찍기)

a=1
c=1
while a<=5:
    print('{0}{1}'.format(' '*(5-a), '*'*a))
   #print('*'*a) # 답
    a+=1
'''

'''
1. 피보나치 수열을 쭉 나열해보기
p[0] + p[1]
p[1] + p[2]
p[3] + p[4]

숫자가 연속적으로 증가한다. >>> 반복문으로 바꿀 생각
2. 입력숫자보다 피보나치 수열의 맨 마지막 숫자가 작으면 멈춤 p[맨끝] > N - stop
3. 피보나치 수열 중 짝수만 더하기>>> p[i] % 2 == 0 하면 다 더하기

'''

'''
# 피보나치수 중 짝수 더하기 - 파이썬 뒤에서부터
fibo = [0,1]
num = int(input("입력 : "))

while fibo[-1] < num:
    fibo.append(fibo[-1]+fibo[-2])
re = 0;
for i in fibo:
    if i % 2 == 0:
        if i < num:
            re += i 
print(re)
'''
'''
# 피보나치수 중 짝수 더하기 - C 앞에서부터

fibo = [0,1]
num = int(input("입력 : "))
i=0
while fibo[len(fibo)-1] < num:
    fibo.append(fibo[i] + fibo[i+1])
    i +=1
    
re = 0;
for i in fibo:
    if i % 2 == 0:
        if i < num:
            re += i 
print(re)
'''
