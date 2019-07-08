class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = 1
        if num == 0:
            return '0'
        elif num < 0:
            flag = -1
            num = num * -1

        res = ''
        while num > 0:
            rem = num % 7
            div = num // 7

            res += str(rem)
            num = div

        if flag == -1:
            res += '-'
        return res[::-1]
