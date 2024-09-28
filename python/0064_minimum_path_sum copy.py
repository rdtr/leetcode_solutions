class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        elif not b:
            return a
        
        if len(a) < len(b):
            a, b = b, a
        
        res = []
        co = 0
        for i in range(0, len(a)):
            bi = "0"
            if len(b) - 1 - i >= 0:
                bi = b[len(b) - 1 - i]
            ai = a[len(a) - 1 - i]

            if ai == "1" and bi == "1":
                if co == 0:
                    res.append("0")
                else:
                    res.append("1")
                co = 1
            elif (ai == "0" and bi == "1") or (ai == "1" and bi == "0"):
                if co == 0:
                    res.append("1")
                else:
                    res.append("0")
                    co = 1
            else:
                if co == 0:
                    res.append("0")
                else:
                    res.append("1")
                    co = 0
        
        if co == 1:
            res.append("1")
        
        return "".join(res[::-1])





