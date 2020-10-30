'''
#버블정렬

ex = [1,5,7,3,4,20,15,9]
ch = True # while문 제어 변수
count = 0 # 대소 비교를 통해 자리바꿈을 확인하는 변수, 자리를 바꾸면 1씩 더함
while ch :
    for i in range(len(ex)-1):
        if ex[i] < ex[i+1]:
            tmp = ex[i]
            ex[i] = ex[i+1]
            ex[i+1] = tmp           
            count+=1            
    if not count > 0:        
        ch = False  
    
    print(count)
    count = 0                  

print(ex)

'''


#자판기 프로그램
제품명 = 0
가격 = 1

ch = 'y'
money = 0
menu = [["커피",100], ["음료수",300], ["과자",200], ["아스크림",600]]
mc= 0
order = []
admin = ['admin', '123']
print('모드 : 1. 관리자, 2. 고객')
sel = int(input('모드 선택 : ' ))
if sel == 1 :
    print("관리자모드")
    print("1. 메뉴 추가, 2. 판매실적")
    
elif sel == 2:

    money = int(input("돈을 넣어주세요 : "))

    while ch =='y' or ch == 'Y' :    
        print('남은금액 : {0} 원'.format(money))
        print("    판매물품    ")
        out = 0 
        for num in range (len(menu)) : # 메뉴 표시
            if money >= menu[num][가격]:
                print(" {0}. {1} : {2}원".format(num+1, menu[num][제품명], menu[num][가격]))
                out += 1
                
        if out > 0 : 
            choice = int(input("메뉴선택 : "))
            if money >= menu[choice-1][가격] :        
                money -= menu[choice-1][가격]          

                count =0
               
                if len(order) == 0 :
                    order.append([menu[choice-1][제품명], 1])
                else:            
                    for i in order:                
                        if i[제품명] == menu[choice-1][제품명]:
                            i[1] += 1
                            count += 1
                    if count == 0 :
                         order.append([menu[choice-1][제품명], 1])
                     
            ch = input("더 뽑으시겠습니까?  : ")
        else :
             print("뽑을 메뉴가 없습니다.")
             ch = input("돈을 더 넣으시겠습니까?  : ")
             if ch == 'y' or ch == 'Y' :
                 money += int(input("돈을 넣어주세요 : "))   
    #결과출력
    print('뽑은 물품 : {0}'.format(order))
    print('거스름돈은 {0} 원 입니다.'.format(money))
else:
    print('메뉴의 번호만 선택해 주세요.')
        
