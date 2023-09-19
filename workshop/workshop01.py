
def inputNameAndPrice() :
    name = str(input('ป้อนชื่อสินค้า : '))
    price = float(input('ป้อนต้นทุนสินค้า : '))
    return name,price
   
def calAndShowSellPrice(name,price) : 
    a = format (float(price),".2f")
    print(f'ชื่อสินค้า {name} ราคาต้นทุน {price} บาท ราคาขาย {round(price + price * 10/100)} บาท ' )

name,price = inputNameAndPrice() 

calAndShowSellPrice(name,price) 



