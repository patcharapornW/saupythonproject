def inputInformation() :
    number = int(input(" รหัสพนักงาน : " ))
    name = str(input(" ชื่อพนักงาน : " ))
    sale = float(input(" ยอดขาย : " ))
    return number,name,sale

def checkCommission(sale) :
    if sale >= 1001 or sale <= 2000  :
        return sale * ( 1 / 100 )
    elif sale >= 2001 or sale <= 3000 :
        return sale * ( 3 / 100 )
    elif sale > 3000 :
        return sale * ( 5 / 100 ) 
    else :
        return sale * 0
    
def commission(number,name,checkCommission) :
     print(f' รหัสพนักงาน : {number} ชื่อพนักงาน : {name} ค่าคอมมิชชั่น : {checkCommission(sale):.2f} ')

number,name,sale = inputInformation()

checkCommission(sale)

commission(number,name,checkCommission)
    
