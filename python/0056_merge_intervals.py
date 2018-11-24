class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        
        res = []
        for i, interval in enumerate(intervals):
            if not res:
                res.append(interval)
                continue
                        
            if res[-1].end < interval.start:
                res.append(interval)
            elif res[-1].end <= intervals[i].end:
                res[-1].end = intervals[i].end
        return res
            