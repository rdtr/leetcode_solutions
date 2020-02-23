class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        len1 = len(str1)
        len2 = len(str2)
        if len1 != len2:
            return False

        m = {}
        for i in range(len1):
            ch1, ch2 = str1[i], str2[i]
            if ch1 in m and m[ch1] != ch2:
                return False
            m[ch1] = ch2
        return len(set(m.values())) < 26
