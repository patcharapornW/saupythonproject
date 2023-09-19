def inputX() :
    X = float(input('x :'))
    return X

def Equation(x) :
    y = 2*(X**2) + (2*X) + 1
    print(f'x = {x:.2f} ได้สมการดังนี้ {y:.2f}')
    return x,y

X = inputX() 

Equation(X)

