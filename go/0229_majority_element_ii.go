func majorityElement(nums []int) []int {
	nlen := len(nums)
	if nlen == 0 {
		return []int{}
	}

	var res []int
	quicksort(nums, 0, nlen-1, &res)
	return res
}

func quicksort(nums []int, left, right int, res *[]int) {
	if right-left+1 <= len(nums)/3 {
		return
	}
	var i, j int
	partition(nums, left, right, &i, &j, res)
	quicksort(nums, left, i, res)
	quicksort(nums, j, right, res)
}

func partition(nums []int, left, right int, i, j *int, res *[]int) {
	pivot := nums[left]
	low, mid, high := left, left, right

	for mid <= high {
		if nums[mid] < pivot {
			nums[low], nums[mid] = nums[mid], nums[low]
			low++
			mid++
		} else if nums[mid] > pivot {
			nums[high], nums[mid] = nums[mid], nums[high]
			high--
		} else {
			mid++
		}
	}

	if mid-low > len(nums)/3 {
		*res = append(*res, pivot)
	}
	*i, *j = low-1, high+1
}