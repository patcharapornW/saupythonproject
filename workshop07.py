def inputNumber() :
    random = int(input(" ป้อนตัวเลขที่ต้องการทาย : "))
    Bingo = 25
    return random,Bingo

def GameBingo (random,Bingo) :
    if random  == Bingo :
        print(" Correct, You are the winner ")
    else :
        print(" Not Correct !!! ")

random,Bingo = inputNumber()

GameBingo(random,Bingo)