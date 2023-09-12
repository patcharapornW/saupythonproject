id_emp = input("รหัสพนักงาน : ")
name_emp = input("ชื่อพนักงาน : ")
salary_emp = float(input("เงินเดือน : "))

total = salary_emp - (salary_emp * 7 / 100) - 500

print(f'คุณ {name_emp} รหัส {id_emp} เงินเดือนสุทธิ : {total} บาท')
