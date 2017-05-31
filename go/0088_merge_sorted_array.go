func merge(nums1 []int, m int, nums2 []int, n int) {
	if m == 0 {
		copy(nums1[:n], nums2[:n])
		return
	}

	start := 0
OUTER:
	for i := 0; i < n; i++ {
		for j := start; j < m; j++ {
			if nums1[j] >= nums2[i] {
				// insert nums2[i] to j th index of nums1
				copy(nums1[j+1:], nums1[j:]) // shift nums1[j:] by one to right
				nums1[j] = nums2[i]
				start, m = j, m+1
				continue OUTER
			}
		}
		copy(nums1[m:m+n-i], nums2[i:])
		break
	}
}
