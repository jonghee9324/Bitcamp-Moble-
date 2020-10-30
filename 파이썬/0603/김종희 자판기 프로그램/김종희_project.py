#자판기 프로그램



ch = 'y'    # 고객의 실행여부 판단 변수
adch = 'n'  # 관리자의 실행여부 판단 변수
money = 0
menu = [["커피",100, 10,0], ["음료수",300,10 ,0], ["과자",200, 10, 0], ["아스크림",600, 10, 0]]
order = []
admin = ['admin', '123']


print('모드 : 1. 관리자, 2. 고객')
sel = int(input('모드 선택 : ' ))

if sel == 1 :
    print("관리자모드")
    ID = input("아이디입력 : ")
    PASS = input("패스워드 입력  : ")
    if ID == admin[0] and PASS == admin[1]:
        while adch =='n' or adch == 'N' :   
            print("1. 메뉴 추가, 2. 판매실적확인, 3. 재고관리")
            choice = int(input("메뉴입력 : "))
            if choice == 1:
                name = input("추가 할 제품명 입력 : ")
                price = int(input("제품 가격 입력 : "))
                menu.append([name, price, 10, 0])
                for num in range (len(menu)) : # 메뉴 표시                
                    print(" {0}. {1} : {2}원".format(num+1, menu[num][제품명], menu[num][가격]))
                    

            elif choice == 2:   # 파일 입출력으로 보완
                print('판매실적 확인')
                for i in menu:
                    print("제품명 : {0}, 판매량 : {1}, 총 판매금액 : {2}".format(i[제품명], i[판매량], i[판매량]*i[가격]))
                    
                
            elif choice == 3:   # 파일 입출력을 통해 기능 추가 보완
                print("남은재고확인")
                for i in range (len(menu)):
                    print("{0}. 제품명 : {1}, 남은수량 : {2}".format(i+1, menu[i][제품명], menu[i][재고]))                  
                choice = int(input("재고를 추가할 상품을 선택해주세요  : "))
                EA = int(input("추가할 재고량을 입력해주세요  : "))
                menu[choice-1][재고] += EA
                for i in range (len(menu)):
                    print("{0}. 제품명 : {1}, 남은수량 : {2}".format(i+1, menu[i][제품명], menu[i][재고]))
                        
            else:
                print("메뉴 번호만 입력하세요")
            
            adch = input("관리자 모드를 종료 하시겠습니까?(y/n)  : ")    
    else:
        print("아이디 비번 확인")
    
    
elif sel == 2:

    money = int(input("돈을 넣어주세요 : "))

    while ch =='y' or ch == 'Y' :    
        print('남은금액 : {0} 원'.format(money))
        print("    판매물품    ")
        out = 0 # 메뉴 출력이 됐는지 확인하는 변수 
        for num in range (len(menu)) : # 메뉴 표시
            if money >= menu[num][가격] and menu[num][재고] > 0:
                print(" {0}. {1} : {2}원".format(num+1, menu[num][제품명], menu[num][가격]))
                out += 1
            
        if out > 0 : # 1개라도 메뉴가 출력되면 메뉴를 구매할 수 있는 기능 제공
            choice = int(input("메뉴선택 : "))
            if choice >=1 and choice <= len(menu):
                EA = int(input("구매할 수량을 입력해주세요   : "))
                if money >= menu[choice-1][가격]*EA and EA <= menu[choice-1][재고]:        
                    money -= menu[choice-1][가격]*EA
                    menu[choice-1][재고] -= EA
                
                    count =0   # order에서 구매한 품목이 있는지 없는지 확인하는 변수
                                  #(0 : order에 구매 품목없음, 0 이상: 품목 존재)
                   
                    if len(order) == 0 :
                        order.append([menu[choice-1][제품명], EA])
                    else:            
                        for i in order:                
                            if i[제품명] == menu[choice-1][제품명]:
                                i[1] += EA
                                count += 1
                        if count == 0 : # 카운터가 0 이기 때문에 order리스트에 구매 폼목의 구매내역이 없어 만들어 
                             order.append([menu[choice-1][제품명], EA])
                else:
                    print("금액 또는 재고가 부족합니다.")
            else:
                print("메뉴번호만 입력해주세요.")
                     
            ch = input("더 뽑으시겠습니까?(y/n)  : ")
        else :
             print("뽑을 메뉴가 없습니다.")
             ch = input("돈을 더 넣으시겠습니까? (y/n) : ")
             if ch == 'y' or ch == 'Y' :
                 money += int(input("돈을 넣어주세요 : "))   
    #결과출력
    print('뽑은 물품 : {0}'.format(order))
    print('거스름돈은 {0} 원 입니다.'.format(money))
else:
    print('메뉴의 번호만 선택해 주세요.')
        
