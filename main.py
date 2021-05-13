import os
import time
import toBinary
import codeValidator
import encDec

def clr():
    os.system("clear")

def binInisialisation(Arr):
    tempArr = Arr
    
    for i in range(0, 8):
        tempBin = "00000000"
        tempBin = tempBin[0:(8-i)] + "1" + tempBin
        tempArr.append(tempBin[0:8])

    return tempArr

def main():
    _code = ["0", False]
    binArr = binInisialisation([])
    hashDigest = []
    xorMess = ""

    mess = input("Enter message: ")
    messDigest = toBinary.toBinary(mess)

    while _code[1] == False:
        encCode = input("enter code: ")
        _code = codeValidator.Validate(encCode)

    encCode = _code[0]
    for i in range(0,7):
        x = int(encCode[i])
        if x > 7:
            x = 0
        hashDigest.append(binArr[x])
        
    xorMess = encDec.encDec(messDigest, hashDigest)

    print(" \nenc'd/dec'd message:")
    print(xorMess)

clr()
main()
