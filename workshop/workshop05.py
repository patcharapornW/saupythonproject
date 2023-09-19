def inputInformation() :
    number = int(input('รหัสพนักงาน : '))
    name = str(input('ฃื่อพนักงาน : '))
    total = float(input('เงินเดือน : '))
    return number,name,total

def TotalAndTax(number,name,total) :
    print(f'รหัสพนักงาน {number} คุณ {name} เงินเดือนปกติ {total} หักภาษี 7% และ ประกันสังคม 500 บาท คิดเป็นเงินเดือนสุทธิ {total -(total * 7/100)- 500:.2f}')
    return total -(total * 7/100)- 500 

number,name,total = inputInformation()

TotalAndTax(number,name,total)