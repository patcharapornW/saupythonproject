def inputInformation() :
    Name = str(input('ชื่อผู้กู้ : '))
    LoanAmout = float(input('จำนวนเงินกู้ : '))
    return Name,LoanAmout

def InterestRate(Name,LoanAmout) :
    if LoanAmout > 1000 :
        print(f'คุณ {Name} จำนวนเงินกู้ {LoanAmout} อัตราดอกเบี้ยร้อยละ 2.5 ของเงินกู้ ')
    else :
        print(f'คุณ {Name} จำนวนเงินกู้ {LoanAmout} อัตราดอกเบี้ยร้อยละ 5.5 ของเงินกู้ ')


Name,LoanAmout = inputInformation() 

InterestRate(Name,LoanAmout)

