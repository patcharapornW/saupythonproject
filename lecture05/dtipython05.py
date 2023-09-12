#คำนวณเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน และแสดงเงินเงินที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชัน ขอ 2 ฟังก์ชัน

#cast/conversion

#รับค่าข้อมูล
def inputMoneyPerson( ) :
    money = float( input('ป้อนเงิน : '))
    person = int( input('ป้อนคน : '))
    return money, person 

#คำนวณ แล้วแสดงผลออกมา
def calAndShowMoneyShare(money, person) : 
    a = format(float(money),".2f")
    #เงิน ขอทศนิยม 2 ตำแหน่ง แชร์กันขอเป็นเลขจำนวนเต็มปัดขึ้น
    print(f'จำนวนเงิน {money:.2f} บาท คน {person} คน แชร์กันคนละ {round(money/person)} บาท')
    print("จำนวนเงิน",a,"บาท คน",(person),"คน แชร์กันคนละ",round(money/person),"บาท") #ใช้ ,
    print("จำนวนเงิน"+" "+str(a)+" "+"บาท คน"+" "+str(person)+" "+"คน แชร์กันคนละ"+" "+str(round(money/person))+" "+"บาท") #ใช้ +
    print('จำนวนเงิน {:.2f} บาท คน {} คน แชร์กันคนละ {} บาท '.format(money, person, (round(money/person )))) #ใช้เมธอด format
    print('จำนวนเงิน %.2f บาท คน %d คน แชร์กันคนละ %d บาท '%(money, person, (round(money/person )))) #ใช้ %
    
money, person = inputMoneyPerson( )

calAndShowMoneyShare( money, person )
