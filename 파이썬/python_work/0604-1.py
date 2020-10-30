'''
#버블정렬
한꺼번에 줄이려고 하지말것,
버블정렬 구하는 과정
1. if 문으로 한 번 나열시키기
2. if 문이 반복되는 것을 알고 반복문을 추가시키기
3. 그 와중에도 리스트 내용이 반복되기 때문에 함수로 만들어 줄이기
'''

L = [7,4,1,6,3]
check = False

while check :
    if check == True:
        for x in range(len(L)):
            if L[x] < L[x+1]:
                tmp = L[x]
                L[x]  = L[x+1]
                L[x+1] = tmp
                check = True
