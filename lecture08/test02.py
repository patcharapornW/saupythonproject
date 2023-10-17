# list มีลำดับ  
my_list = [10, 20, 10, 'Hi', True, [20, 'Hello'], (10,20), (10,20)]

# Tuple มีลำดับ
my_tuple = (10, 20, 10, 'Hi' , True, [20, 'Hello'], [10,20], {10,20})

# set เป็นข้อมูลที่ไม่มีลำดับ ข้อมูลที่ซ้ำถือว่าเป็นข้อมูลเดียวกัน
my_set = {10, 20, 10, 'Hi' , True, (10,20)}
                    
                    # Key คือ index คือ ตัวฃี้อ้างอิงไปยัง value
                    # value คือ ค่าข้อมูลที่สามารถเอาไปใช้งาน
                    # เวลาจะใช้งาน value ต้องผ่าน Key
#  Dictionary --->> Key:Value / key -> string-Number / Value-> Everting
my_dict = {'name' :'สมชาย', 'age' : 20, 555:999, 'flag':True }
print(my_dict['name'])
print(my_dict['age'] + my_dict[555])
# เปลี่ยนข้อมูล (ผ่าน Key)
my_dict['name'] = 'สมหญิง'
my_dict['major'] = 'DTI'
print(my_dict)
my_dict.pop('name')
my_dict.pop(555)
print(my_dict)
# popitem เอาตัวสุดท้ายออก
my_dict.popitem()
print(my_dict) 

for data in my_dict :
    print(data, end=' ')

print()

for data in my_dict.keys() :
    print(data, end=' ')

print()

for data in my_dict.values() :
    print(data, end=' ')
    
my_dict1 = {'a':10, 'b':20, 'c':30}

my_dict2 = my_dict1

my_dict3 = my_dict1.copy()

print()
print(my_dict2)
print(my_dict3)
my_dict2['a'] = 999
my_dict3['a'] = 888
print('------------------------')
print(my_dict1)
print(my_dict2)
print(my_dict3)