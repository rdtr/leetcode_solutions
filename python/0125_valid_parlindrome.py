class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < len(s) and not self.isValid(s[left]):
                left += 1
            while right >= 0 and not self.isValid(s[right]):
                right -= 1

            if left >= right:
                break

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isValid(self, ch):
        return ('a' <= ch and ch <= 'z') or ('A' <= ch and ch <= 'Z') or ('0' <= ch and ch <= '9')
