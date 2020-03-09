class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        neg = ''
        if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
            neg = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)

        res = []

        i = -1
        while numerator >= denominator:
            d, r = numerator // denominator, numerator % denominator
            res.append(str(d))
            numerator = r
            i += 1
        if numerator == 0:
            return neg + ''.join(res)

        if not res:
            res.append('0')
            i = 0
        res.append('.')
        i += 1
        numerator *= 10

        seen = {}
        while numerator != 0:
            d, r = numerator // denominator, numerator % denominator
            if (r, d) in seen:
                res.insert(seen[(r, d)], '(')
                res.append(')')
                return neg + ''.join(res)
            else:
                res.append(str(d))
                i += 1
                seen[(r, d)] = i
                numerator = r * 10
        return neg + ''.join(res)
