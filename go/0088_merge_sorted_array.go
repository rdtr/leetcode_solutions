func merge(nums1 []int, m int, nums2 []int, n int) {
	cur := n + m - 1
	cur1, cur2 := m-1, n-1

	for cur1 >= 0 || cur2 >= 0 {
		switch {
		case cur1 < 0:
			nums1[cur] = nums2[cur2]
			cur--
			cur2--
		case cur2 < 0:
			nums1[cur] = nums1[cur1]
			cur--
			cur1--
		default:
			if nums1[cur1] > nums2[cur2] {
				nums1[cur] = nums1[cur1]
				cur1--
			} else {
				nums1[cur] = nums2[cur2]
				cur2--
			}
			cur--
		}
	}
}