class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        nlen = len(num)
        if nlen == 0:
            return False

        left = 0
        right = nlen - 1
        while left <= right:
            if left == right:
                return num[left] == '0' or num[left] == '1' or num[left] == '8'

            if not self.isOK(num[left], num[right]):
                return False
            left += 1
            right -= 1
        return True

    def isOK(self, ch1, ch2):
        if ch1 == '0' and ch2 == '0':
            return True
        elif ch1 == '1' and ch2 == '1':
            return True
        elif ch1 == '6' and ch2 == '9':
            return True
        elif ch1 == '8' and ch2 == '8':
            return True
        elif ch1 == '9' and ch2 == '6':
            return True
        return False
