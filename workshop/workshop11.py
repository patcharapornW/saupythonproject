def inputBill() :
    user = str(input(" ชื่อผู้ใช้ : "))
    number = (input(" เบอร์โทรศัพท์ : "))
    minutes = float(input(" จำนวนนาที : "))
    return user,number,minutes

def Amount(number,minutes) :
    if minutes >= 1 or minutes <= 15:
        return minutes * 5
    elif minutes >= 16 or minutes <=30:
        return minutes * 3
    else:
        return minutes * 1.5

def showBill(user,number,minutes,Amount):
    print(f'ชื่อผู้ใช้ : {user} เบอร์โทรศัพท์ : {number} จำนวนนาที : {minutes} ค่าบริการ : {Amount(number,minutes)}')

user,number,minutes = inputBill()
Amount(number,minutes)
showBill(user,number,minutes,Amount)