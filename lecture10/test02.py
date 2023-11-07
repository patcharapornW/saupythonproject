# เขียนข้อมูลลงไฟล์ 
# เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti = open('myfile01.txt','w', encoding='utf-8') 

f_dti.write('Hello...')
f_dti.write('Hi....\n')
f_dti.write('สวัสดีทุกคน...\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')


