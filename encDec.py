def encDec(messageDigest, hashDigest):
     n = 0
     xorMess = ""

     for i in messageDigest:
          if n == 7:
               n = 0

          rawBinMess = int(i, 2) ^ int(hashDigest[n], 2)

          if rawBinMess <= 31 or rawBinMess == 127:
               xorMess += " " + hex(rawBinMess) + " "
          else:
               xorMess += chr(rawBinMess)

          n += 1
     return xorMess
     
     
     



