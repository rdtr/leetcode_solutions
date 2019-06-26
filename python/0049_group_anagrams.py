from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(lambda: [])
        for s in strs:
            ht = [0] * 26
            for ch in s:
                ht[ord(ch) - ord('a')] += 1
            mp[self.stringify(ht)].append(s)

        return [x for x in mp.values()]

    def stringify(self, ht):
        res = ''
        for i in range(26):
            if ht[i] > 0:
                res += chr(i + ord('a'))
                res += str(ht[i])
        return res