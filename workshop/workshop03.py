def NameProduct() :
    name = str(input('ชื่อสินค้า : '))
    price = float(input('ราคาสินค้า : '))
    return name,price

def TotalAndTax(name,price) : 
    print(f'ชื่อสินค้า {name} ราคาสินค้า {price} ภาษีคิดเป็น {price *(7/100):.2f}' )
    return price * 7/100

name,price = NameProduct()

TotalAndTax(name,price)