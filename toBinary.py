
def toBinary(encMess):
    binArr = []
    binVal = ""
    index = 0

    if "0x" in encMess:
        while index != len(encMess):
            if encMess[index] == " " and encMess[index+5] == " ":
                temp = encMess[index:index+6].strip()
                if "0x" in temp:
                    binVal = bin(int(temp[2:], 16))[2:].zfill(8)
                    index += 6
                else:
                    binVal = bin(ord(encMess[index]))[2:].zfill(8)
                    index += 1
                binArr.append(binVal)
            else:
                binVal = bin(ord(encMess[index]))[2:].zfill(8)
                index += 1
                binArr.append(binVal)
    else:
        while index != len(encMess):
            binVal = bin(ord(encMess[index]))[2:].zfill(8)
            binArr.append(binVal)
            index += 1

    return (binArr)