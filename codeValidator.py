def codeDiverger(code, LR):
    if LR % 2 == 0:
        return (code + "0")
    else:
        return ("0" + code)

def codeConverger(code):
    n1 = int(code[0])
    n2 = int(code[-1])

    tcode = code[1:-1]

    if n1 > n2:
        tcode += str(abs(n1 - n2))
    else:
        tcode = str(abs(n1 - n2)) + tcode

    return tcode

def Validate(code):
    valid = False
    tcode = code
    _x = 2
    if tcode.isnumeric():
        if len(tcode) < 7:
            while len(tcode) != 7:
                tcode = codeDiverger(tcode, _x)
                _x += 1
        elif len(tcode) > 7:
            while len(tcode) != 7:
                tcode = codeConverger(tcode)
        valid = True
    else:
        print("enter valid code bitch!")
        input("")
    
    temp = [tcode, valid]
    return temp