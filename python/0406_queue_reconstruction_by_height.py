class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people.sort(key=lambda p: (-p[0], p[1]))

        blocks = [[]]
        for p in people:
            cnt = 0
            height, index = p[0], p[1]
            for i, block in enumerate(blocks):
                if index - len(block) <= 0:
                    break
                index -= len(block)
            block.insert(index, p)

            if len(block) * len(block) > len(people):
                blocks.insert(i + 1, block[len(block) // 2:])
                blocks[i] = block[:len(block) // 2]

        res = []
        for block in blocks:
            for b in block:
                res.append(b)
        return res
