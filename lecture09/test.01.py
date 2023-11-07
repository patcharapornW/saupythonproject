class Dtitest01 :
    pass 

class Dtitest02 :
    # data/attribute/property/fleid คือ ส่วนแบ่งประเภทหนึ่ง
    infoA = '' 
    infoB = 20

    # method คือ ฟังก์ชันประเภทหนึ่ง
    def showHi(slef) :
        print('Hi...')

    def showInfoAandB(self) :
        print(self.infoA)
        print(self.infoB)
        
# สร้าง object
objA = Dtitest02()
objB = Dtitest02()
sombat = Dtitest02()

objA.infoA = 'xxx'
objB.infoB = 100
print(objA.infoB + objB.infoB)

sombat.showInfoAandB() 
