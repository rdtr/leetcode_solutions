import heapq

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        m = {}
        for word in words:
            if word in m:
                m[word] += 1
            else:
                m[word] = 1
        
        counts = [(-v, k) for k, v in m.items()]
        heapq.heapify(counts)
        
        res = [0] * k
        for i in range(k):
            res[i] = heapq.heappop(counts)[1]
        return res