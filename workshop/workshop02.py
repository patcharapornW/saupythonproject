def inputStudentNumber( )  :
    number = int(input('รหัสนักเรียน : '))
    name = str(input('ชื่อนักเรียน : '))
    point1 = float(input('คะแนนครั้งที่หนึ่ง : '))
    point2 = float(input('คะแนนครั้งที่สอง : '))
    point3 = float(input('คะแนนครั้งที่สาม : '))
    return number,name,point1,point2,point3

def AllPoint(number,name,point1,point2,point3) :
    print(f'รหัสนักเรียน {number} ชื่อ {name} ได้คะแนน = {(point1+ point2 + point3)/3:.2f}')
    return point1 + point2 + point3/3

number,name,point1,point2,point3 = inputStudentNumber( )  

AllPoint(number,name,point1,point2,point3) 
