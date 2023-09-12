#โปรแแกรมคำนวณหาพื้นที่วงกลม เส้นรอบวง และปริมาตรทรงกลม จากรัศมีที่ป้อนโดยผู้ใช้ททางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ

#ขอ 5 ฟังก์ชัน
import math 

#inputRadius
def inputRadius() :
    # r = input('ป้อนรัศมี')
    # หรือ r = float(input('ป้อนรัศมี : '))
    # return r
    # return input('ป้อนรัศมี : ')
    return float (input('ป้อนรัศมี : '))


#calAreaCircle
def calAreaCircle( r ) : 
    #area = math.pi * r ** 2
    #area = math.pi * math.pow(r,2)
    return math.pi * r ** 2
    #print('พื้นที่วงกลม {:.4f} เส้นรอบวง {:.4f} ปริมาตรทรงกลม {:.4f}'.format(calAreaCircle, calRonundCircle, calCubeCircle))
    


#calRoundCircle 2 * pi * r
def calRonundCircle( r ) :
    return 2 * math.pi * r

#calCubeCircle 4/3 * pi * r *** 3
def calCubeCircle(r ) :
    return 4/3 * math.pi * math.pow(r,3) 

    

#showResul ขอทั้งหมดทศนิยม 4 ตำแหน่ง
#พื้นที่วงกลม ???? เส้นรอบวง ???? ปริมาตรทรงกลมเป็น ???? 
def showresult() :
    r = inputRadius()
    print(f'พื้นที่วงกลม {calAreaCircle( r ):.4f} เส้นรอบวง {calRonundCircle( r ):.4f} ปริมาตรทรงกลม {calCubeCircle(r ):.4f}')

showresult()