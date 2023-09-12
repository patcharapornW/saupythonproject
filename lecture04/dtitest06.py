name_product = input("ป้อนชื่อสินค้า : ")
price_product = float(input("ป้อนราคาสินค้า : "))
sell_price = price_product + price_product * 10 /100

print("ราคาต้นทุน {:.2f} บาท ราคาขาย {:.2f} บาท".format(price_product,sell_price))
print(f'ราคาต้นทุน {price_product} บาท ราคาขาย {sell_price} บาท')
print("ราคาต้นทุน",(price_product), "บาท ราคาขาย",(sell_price),"บาท")
print("ราคาต้นทุน"+" "+str(price_product)+" "+"บาท ราคาขาย"+" "+str(sell_price)+" " +"บาท")