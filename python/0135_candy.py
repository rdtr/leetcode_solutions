class Solution:
    def candy(self, ratings: List[int]) -> int:
        rlen = len(ratings)
        if rlen == 0:
            return 0

        l2r, r2l = [0] * rlen, [0] * rlen
        for i in range(1, rlen):
            if ratings[i] > ratings[i - 1]:
                l2r[i] = 1
            if ratings[rlen - 1 - i] > ratings[rlen - i]:
                r2l[rlen - i - 1] = 1

        candies = [0] * rlen
        for i in range(rlen):
            if i == 0:
                candies[i] = 1
                continue
            if l2r[i] > 0:
                candies[i] = candies[i - 1] + 1
            else:
                candies[i] = 1
        for i in range(rlen - 1, -1, -1):
            if i == rlen - 1:
                continue
            if r2l[i] > 0 and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)
