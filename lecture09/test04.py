# คุณสมบัติเด่น Encapsulation (ห่อหุ้ม data/attribute/field/property)
class DtiTest05 :
    #  data
    infoA = 10 # ไม่ได้ห่อหุ้ม
    __infoB = 20 # 
    
    def __init__(self, infoC, infoD) :
        self.infoC = infoC      #ไม่ได้ห่อหุ้ม
        self.__infoD = infoD     #Encap ดูจาก __?? -> เป็นการกำหนดการเข้าถึงให้เป็น private

    # เมื่อใดก็ตาม Encap จะต้องมีเมธอต 2 ตัวนี้เสมอ คือ get,set
    def setInfoB(self, infoB) : #กำหนดค่าให้กับ data
        self.__infoB = infoB

    def getInfoB(self) : #เอาค่า data ไปใช้
        return self.__infoB
    
    def setInfoD(self, infoD) :
        self.__infoD = infoD
    
    def getInfoD(self) :
        return self.__infoD
    
    def showInfo(self):
        print(self.infoA, end='')
        print(self.__infoB, end='')
        print(self.infoC, end='')
        print(self.__infoD)
        print('-------------------')

ob1 = DtiTest05(30, 40)
ob2 = DtiTest05(30, 100)
ob1.showInfo()
ob1.infoA = 555
ob1.setInfoB(999)
ob1.showInfo()
print(ob1.getInfoB() + ob1.getInfoD())