from collections import deque


class Solution:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)

        dist = 0
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    for j in range(len(Solution.alphabets)):
                        newWord = word[:i] + Solution.alphabets[j] + word[i + 1:]
                        if newWord in wordSet:
                            if newWord == endWord:
                                return dist + 1 + 1
                            wordSet.remove(newWord)
                            q.append(newWord)
            dist += 1
        return 0
