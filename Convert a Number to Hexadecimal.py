class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        hexDec = {10 : 'a', 11 : 'b', 12 : 'c', 13 : 'd', 14 : 'e', 15 : 'f' }
        result = ""
        if num > 0:
            while num != 0:
                remainder = num % 16
                if remainder in hexDec:
                    result += str(hexDec[remainder])
                else:
                    result += str(remainder)
                num //= 16
            return result[::-1]
        else:
            d1 = {'0000':0,'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':'a','1011':'b','1100':'c','1101':'d','1110':'e','1111':'f'}
            num1 = -num
            carry = 1
            b1 = list(bin(num1)[2:].zfill(32))
            for i in range(len(b1)):
                if b1[i] == "1":
                    b1[i] = "0"
                else:
                    b1[i] = "1"
            for i in range(len(b1)):
                if b1[-i-1] != '1':
                    b1[-i-1] = str(int(b1[-i-1])+carry)
                    carry = 0
                elif carry == 1 and b1[-i-1] == '1':
                    b1[-i-1] = '0'
                    carry = 1
            if carry == 1:
                b1.insert(0, '1')
            result = "".join(b1)
            s1 = ""
            for i in range(0, len(result), 4):
                s1 += str(d1[result[i:i+4]])  
        return s1            
        
