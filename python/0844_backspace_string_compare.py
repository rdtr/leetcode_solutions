class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s, t = len(S) - 1, len(T) - 1
        while True:
            sback, tback = 0, 0
            while (S[s] == '#' or sback > 0) and s > -1:
                if S[s] == '#':
                    sback += 1
                else:
                    sback -= 1
                s -= 1
            while (T[t] == '#' or tback > 0) and t > -1:
                if T[t] == '#':
                    tback += 1
                else:
                    tback -= 1
                t -= 1

            if s == -1 and t == -1:
                return True
            elif s > -1 and t > -1 and S[s] == T[t]:
                s -= 1
                t -= 1
            else:
                return False