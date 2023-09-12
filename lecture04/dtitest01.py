width = float(input("ป้อนความกว้าง : "))
long = float(input("ป้อนความยาว : "))
high = float(input("ป้อนความสูง : "))
print('------------------------')
#คำนวณ
a = width * long * 2
b = width * high * 2
c =  width * width * 2
d = round(a+b+c)/5
print("พื้้นที่ทั้งหมด",round(a + b + c)/5)
print("พื้นที่ทั้งหมด"+" "+str(d))
print(f'พื้นที่ทั้งหมด {d}')
print("พื้นที่ทั้งหมด {}".format(d))



#กล่องสี่เหลี่ยมที่มีความกว้าง N ยาว สูง N ต้องใช้สีทั้งหมด N แกนลอน 




