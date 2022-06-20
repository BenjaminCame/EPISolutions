# Chapter 4,
# 4.1 Compute the parity of a binary word

from cgitb import lookup
from tabnanny import check
import re
import string


class parity:


    def checkParity(input) -> bool:
        lookup = {        
            "0000":0,
            "0001":1,
            "0010":1,
            "0100":1,
            "1000":1,
            "1001":0,
            "1010":0,
            "1100":0,
            "1101":1,
            "1110":1,
            "1111":0,
        }
        input = str(input)
        parity = 0

        while(len(input)%4 != 0):# make sure input in divisable my 4
            input = ''.join('0'+input)
        
        bits = re.findall('....',input)#break into 16 bit words for lookup table

        for bit in bits:
            parity += lookup[bit]
            print(bit, lookup[bit], parity)
    
        return parity%2

if __name__ == "__main__":
    print(parity.checkParity(100110011001101))



 