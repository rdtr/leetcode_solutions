package main

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if l := len(nums1) + len(nums2); l%2 == 0 {
		return (findKth(nums1, nums2, l/2-1) + findKth(nums1, nums2, l/2)) / 2.0
	} else {
		return findKth(nums1, nums2, l/2)
	}
}

func findKth(nums1 []int, nums2 []int, k int) float64 {
	for {
		l1, l2 := len(nums1), len(nums2)
		m1, m2 := l1/2, l2/2

		if l1 == 0 {
			return float64(nums2[k])
		} else if l2 == 0 {
			return float64(nums1[k])
		} else if k == 0 {
			if n1, n2 := nums1[0], nums2[0]; n1 <= n2 {
				return float64(n1)
			} else {
				return float64(n2)
			}
		}

		if k <= m1+m2 {
			if nums1[m1] <= nums2[m2] {
				nums2 = nums2[:m2]
			} else {
				nums1 = nums1[:m1]
			}
		} else {
			if nums1[m1] <= nums2[m2] {
				nums1 = nums1[m1+1:]
				k -= m1 + 1
			} else {
				nums2 = nums2[m2+1:]
				k -= m2 + 1
			}
		}
	}
}
