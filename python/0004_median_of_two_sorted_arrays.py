class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        if (l1+l2)%2 == 0:
            return (self.findKth(nums1, nums2, (l1+l2)/2 - 1) + self.findKth(nums1, nums2, (l1+l2)/2)) / 2.0
        return self.findKth(nums1, nums2, (l1+l2)/2)
    
    def findKth(self, nums1, nums2, k):
        while True:
            l1, l2 = len(nums1), len(nums2)
            m1, m2 = l1/2, l2/2
        
            if l1 == 0:
                return nums2[k]
            elif l2 == 0:
                return nums1[k]
            elif k == 0:
                if nums1[0] < nums2[0]:
                    return nums1[0]
                return nums2[0]
            
            if k <= m1 + m2:
                if nums1[m1] <= nums2[m2]:
                    nums2 = nums2[:m2]
                else:
                    nums1 = nums1[:m1]
            else:
                if nums1[m1] <= nums2[m2]:
                    nums1 = nums1[m1+1:]
                    k -= m1+1
                else:
                    nums2 = nums2[m2+1:]
                    k -= m2+1
                