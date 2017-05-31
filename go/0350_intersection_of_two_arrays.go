import "sort"

func intersect(nums1 []int, nums2 []int) []int {
	m := make(map[int]int)
	for _, n := range nums1 {
		if count, ok := m[n]; !ok {
			m[n] = 1
		} else {
			m[n] = count + 1
		}
	}

	var res []int
	for _, n := range nums2 {
		if count, ok := m[n]; ok && count > 0 {
			res = append(res, n)
			m[n] = count - 1
		}
	}
	return res
}

func intersect(nums1 []int, nums2 []int) []int {
	sort.Ints(nums1)
	sort.Ints(nums2)

	var res []int
	for _, n := range nums1 {
		if index := find(nums2, n); index >= 0 && index < len(nums2) && nums2[index] == n {
			res = append(res, n)
			nums2 = nums2[index+1:]
		}
	}
	return res
}

func find(nums []int, n int) int {
	left, right := 0, len(nums)-1
	var mid int
	for left < right {
		mid = left + (right-left)/2
		switch {
		case nums[mid] >= n:
			right = mid
		case nums[mid] < n:
			left = mid + 1
		}
	}
	return right
}