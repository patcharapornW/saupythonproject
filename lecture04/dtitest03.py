#Function แบบที่ 2 - Have parameters/No return
#parameters คือ เป็นตัวแปรประเภทหนึ่ง เอาไส้รับค่ามาใช้เฉพาะในฟังก์ชันนั้นๆ เท่านั้น

def funcA( x, y) : 
    print(f'X  is {x}') 
    print(f'Y  is {y}')
    print(f'Sum {x} + {y} = {x+y}') 

funcA(10,20)#call function ข้อมูลที่ส่งให้ parameters เรียกว่า argument 
funcA(1,4)
print('DTI.....') 
funcA(5,5) 
