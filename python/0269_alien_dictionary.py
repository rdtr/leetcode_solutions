from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(lambda: set())
        incomings = {}
        
        # populate graph
        for i in range(len(words)):
            for ch in words[i]:
                if ch not in incomings:
                    incomings[ch] = 0
            
            if i > 0:
                curWord = words[i]
                prevWord = words[i-1]
                
                added = False
                for j in range(min(len(curWord), len(prevWord))):
                    if curWord[j] == prevWord[j]:
                        continue
                    
                    if curWord[j] not in graph[prevWord[j]]:
                        graph[prevWord[j]].add(curWord[j])
                        incomings[curWord[j]] += 1
                    added = True
                    break
                
                # special case handling such as ["ab", "abc"]
                if not added and len(curWord) < len(prevWord):
                    return ""
                
                    
        chNum = len(incomings)
        
        # topological sort
        starts = deque([])
        for ch, incoming in incomings.items():
            if incoming == 0:
                starts.append(ch)
        
        res = []
        while starts:
            s = starts.popleft()
            res.append(s)
            
            toChs = graph[s]
            for toCh in toChs:
                incomings[toCh] -= 1

                if incomings[toCh] == 0:
                    starts.append(toCh)
            
        if len(res) == chNum:
            return "".join(res)
        return ""
