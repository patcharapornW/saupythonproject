#คำสั่ง return ที่ไม่มีอะไรต่อท้าย หมายถึง การบ่งบอกการทำงานนั้นๆ ว่าเสร็จแล้ว
def example1() :
    print(111)
    print(222)
    return
    print(3333)
    pritn(4444)
    return

# Default parameter
def dtiTest(x, y, z = 20, a = 10) :
    print(f'{x} {y} {z} {a} = {x+y+z+a}')


dtiTest(5, 100)

dtiTest(9, 8, 10)
