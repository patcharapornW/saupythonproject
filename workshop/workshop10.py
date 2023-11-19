def GradeYear() :
    year = int(input(" ป้อนชั้นปี : "))
    return year

def show(year) :
    if year == 1 :
        print(" Welcome Freshman ") 
    elif year == 2 :
        print(" Welcome Sophomore ") 
    elif year == 3 :
        print(" Welcome Junior ") 
    else : 
        print(" Welcome Senior ")

year = GradeYear()
show(year)

