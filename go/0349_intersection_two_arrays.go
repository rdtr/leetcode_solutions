func intersection(nums1 []int, nums2 []int) []int {
	mp := make(map[int]int)
	for _, num := range nums1 {
		if _, ok := mp[num]; !ok {
			mp[num] = 1
		}
	}

	var res []int
	for _, num := range nums2 {
		if cnt, ok := mp[num]; ok && cnt > 0 {
			res = append(res, num)
			mp[num]--
		}
	}
	return res
}