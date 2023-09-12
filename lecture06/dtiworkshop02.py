#โปรแกรมตรวจสอบน้ำหนักรถบรรทุกของด่านชั่งน้ำหนักว่ารถบรรทุกนั้นมีน้ำหนักผ่านเกณฑ์หรือไม่ หากน้ำหนักเกิน 1000 kg ลงมาให้แสดงข้อความว่า "รถน้ำหนักไม่ผ่านเกณฑ์" แต่หากน้ำหนักตั้งแต่ 1000 kg ลงมาให้แสดงข้อความว่า "รถน้ำหนักผ่านเกณฑ์" โดยให้ป้อนทะเบียนรถบรรทุกและน้ำหนักรถบรรทุกทางแป้นพิมพ์

# วิเคราะห์
# มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อจะสร้างเป็น function
# รับค่าทะเบียนรถ น้ำหนักรถ -> inputCarDetial
# ตรวจสอบน้ำหนักรถ และแสดงผล -> checkCarAndShowWeight

def inputCarDetail() :
    carNo = input('ป้อนทะเบียนรถ : ')
    carWeight = float( input('ป้อนน้ำหนักรถ : ') )
    return carNo, carWeight

def checkCarAndShowWeight(carNo, carWweight) :
    if carWeight > 1000 :
        print(f'ทะเบียนรถ {carNo} น้ำหนักไม่ผ่านเกณฑ์')
    else :
        print(f'ทะเบียนรถ {carNo} น้ำหนักผ่านเกณฑ์')

print('---------------------------')
print('--* Truck Check *--')
print('---------------------------')
carNo, carWeight = inputCarDetail() 
print('---------------------------')
checkCarAndShowWeight(carNo, carWeight)
print('---------------------------')