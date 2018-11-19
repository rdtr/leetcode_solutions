class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        end, shouldBreak = 0, False
        while True:
            for i, s in enumerate(strs):
                if end > len(s) - 1:
                    if len(s) == 0:
                        return ''

                    shouldBreak = True
                    break

                if i == 0:
                    c = s[end]
                elif s[end] != c:
                    shouldBreak = True
                    break
            if shouldBreak:
                break
            end += 1
        return strs[0][:end]
