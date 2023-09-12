celsius = float(input("อุณหภูมิ c: "))
fahrenheit = 9 / 5 * celsius + 32

c = format(float(celsius), ".2f")
f = format(float(fahrenheit), ".2f")

print(f"อุณหภูมิ {celsius:.2f} C แปลงเป็น {fahrenheit:.2f} F ")
print("อุณหภูมิ", c, "C", "แปลงเป็น", f, "F")
print("อุณหภูมิ"+" "+str(c)+" "+"C"+" "+"แปลงเป็น"+" "+ str(f) +" "+"F")
print("อุณหภูมิ {:.2f} C แปลงเป็น {:.2f} F ".format(celsius,fahrenheit))
