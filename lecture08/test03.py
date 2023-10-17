# OOP
class DtiSau : 
    # data/ property member ค่าข้อมูล
    stu_name = ''
    score = 0
    gpa = 0

    # method member การทำงาน (เขียนแบบฟังก์ชัน เพียงแต่อยู่ใน class)
    def hiStudent(self) :
        print(f'สวัสดี {self.stu_name}')

    def showScoreAndGpa(self) :
        print(f'คะแนน {self.score} ได้ GPA: {self.gpa}')

# สร้าง Object
obj01 = DtiSau() #ชืื่อคลาสที่มี () เราเรียกว่าเป็นการสั่งให้ constructor ของคลาสทำงาน
obj02 = DtiSau()

obj01.stu_name = 'สมชาย'
obj01.hiStudent()
obj02.stu_name = 'สมหญิง'
obj02.score = 99
obj02.gpa = '3.99'


