#Function 1 : no parameter/no return
def funcA( ) : 
    print('AAA')
    #ไม่ควรเรียก function กันไปมา
    print('BBB')
    #ไม่มีคำสั่ง return 

def funcB( ) :
    print(111)
    funcA( )

funcA( )
funcA( )
funcB( )
