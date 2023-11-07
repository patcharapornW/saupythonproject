f_dti = open('myfile01.txt', 'r', encoding='utf-8')

try :
    data = f_dti.readline()
    print(data, end='')
    data = f_dti.readline()
    print(data, end='')
except Exception : 
    print('ติดต่อ ADmin 025555555')
finally :
    f_dti.close()