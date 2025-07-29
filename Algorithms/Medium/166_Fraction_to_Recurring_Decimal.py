class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
            
        num, den = abs(numerator), abs(denominator)
        result.append(str(num // den))
        
        rem = num % den
        if rem != 0:
            result.append(".")
            rem_pos = {}
            while rem:
                if rem in rem_pos:
                    result.insert(rem_pos[rem], "(")
                    result.append(")")
                    break
                
                rem_pos[rem] = len(result)
                rem *= 10
                digit = rem // den
                result.append(str(digit))
                rem %= den
        
        return "".join(result)
