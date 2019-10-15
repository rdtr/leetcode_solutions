class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [v.lstrip('0') for v in version1.split('.')]
        v2 = [v.lstrip('0') for v in version2.split('.')]

        flg = 1
        if len(v1) > len(v2):
            v1, v2 = v2, v1
            flg = -1

        i = 0
        while i < len(v1):
            n1 = int(v1[i]) if v1[i] else 0
            n2 = int(v2[i]) if v2[i] else 0
            if n1 == n2:
                i += 1
            elif n1 > n2:
                return flg
            else:
                return -flg

        while i < len(v2):
            if v2[i] != '0' and v2[i] != '':
                return -flg
            i += 1
        return 0

