f_dti = open('myfile02.txt','x', encoding='utf-8') 

f_dti.write('SAU')
f_dti.write('DTI......\n')
f_dti.write('ไปก่อนนะ...\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')