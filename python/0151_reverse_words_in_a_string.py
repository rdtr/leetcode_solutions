class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = [t for t in s.split(' ') if t != '']
        self.reverse(arr)
        return ' '.join(arr)

    def reverse(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
