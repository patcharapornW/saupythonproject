def inputInfomation() :
    studentId = input(" รหัสนักเรียน : ")
    studentName = input(" ชื่อนักเรียน : ")
    studentGrade = float(input(" เกรดเฉลี่ย : "))
    return studentId,studentName,studentGrade

def checkStudentGrade(studentId,studentName,studentGrade):
    if studentGrade > 2.00 :
        return f" นักเรียนรหัส {studentId} ชื่อ {studentName} ได้เกรดเฉลี่ย {studentGrade} สอบผ่าน "
    else:
        return f" นักเรียนรหัส {studentId} ชื่อ {studentName} ได้เกรดเฉลี่ย {studentGrade} สอบไม่ผ่าน "

def showStudentGrade() :
    numStudents = int(input(" ป้อนจำนวนนักเรียนที่ต้องการตรวจสอบ : "))

    for i in range(numStudents):
        studentId,studentName,studentGrade = inputInfomation()
        result = checkStudentGrade(studentId,studentName,studentGrade)
        print(result)

showStudentGrade()