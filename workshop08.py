def inputInformation() :
    province = str(input(" ป้อนจังหวัด : "))
    PH = float(input(" ป้อนค่า PH : "))
    return province,PH

def PHvalue(province,PH) :
    if PH == 7 or 8 :
        print(" Result is Normal ")
    elif PH > 8 :
        print(" Result is Acid ")
    else :
        print(" Result is Alkali ")

province,PH = inputInformation()

PHvalue(province,PH)