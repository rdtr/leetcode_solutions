func maxSlidingWindow(nums []int, k int) []int {
	nlen := len(nums)
	if nlen == 0 {
		return []int{}
	}

	// get initial deque from nums[0:k-1]
	deque := []int{0}
	for i := 1; i < k; i++ {
		if len(deque) == 0 || nums[i] >= nums[deque[0]] {
			deque = []int{i}
		} else if nums[i] < nums[deque[len(deque)-1]] {
			deque = append(deque, i)
		} else {
			insert(&deque, nums, i)
		}
	}

	// proceed and update deque
	res := make([]int, nlen-k+1)
	res[0] = nums[deque[0]]
	for i := 1; i < nlen-k+1; i++ {
		idx := i + k - 1

		if deque[0] < i {
			deque = deque[1:]
		}

		if len(deque) == 0 || nums[idx] >= nums[deque[0]] {
			deque = []int{idx}
			res[i] = nums[idx]
		} else if nums[idx] < nums[deque[len(deque)-1]] {
			res[i] = nums[deque[0]]
			deque = append(deque, idx)
		} else {
			res[i] = nums[deque[0]]
			insert(&deque, nums, idx)
		}
	}
	return res
}

// insert inserts nums[index] to deque while searching a place to index,
// where nums[i] > nums[index] suffices for the first time.
func insert(pdeque *[]int, nums []int, index int) {
	deque := *pdeque
	j := len(deque) - 1
	for nums[index] >= nums[deque[j]] {
		j--
	}
	deque[j+1] = index
	deque = deque[:j+2]
	*pdeque = deque
}