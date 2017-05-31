func wiggleSort(nums []int) {
	n := len(nums)
	if n <= 1 {
		return
	}

	median := findKth(nums, 0, n-1, (n-1)/2)

	left := 0
	right := n - 1
	j := 0
	for j <= right {
		if nums[j] < nums[median] {
			nums[j], nums[left] = nums[left], nums[j]
			j++
			left++
		} else if nums[j] > nums[median] {
			nums[j], nums[right] = nums[right], nums[j]
			right--
		} else {
			j++
		}
	}

	temp := make([]int, n)
	copy(temp, nums)

	left = (n - 1) / 2
	right = n - 1
	for i := 0; i < n; i++ {
		if (i & 1) == 0 {
			nums[i] = temp[left]
			left--
		} else {
			nums[i] = temp[right]
			right--
		}
	}
}

func findKth(nums []int, low, high int, k int) int {
	if low >= high {
		return low
	}

	pivot := partition(nums, low, high)
	if k == pivot {
		return pivot
	}

	if pivot > k {
		return findKth(nums, low, pivot-1, k)
	} else {
		return findKth(nums, pivot+1, high, k)
	}
}

func partition(nums []int, low, high int) int {
	pivot := nums[low]
	i, j := low+1, high
	for i <= j {
		for i <= j && nums[i] < pivot {
			i++
		}
		for i <= j && nums[j] >= pivot {
			j--
		}

		if i <= j {
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	nums[low], nums[j] = nums[j], nums
	return j
}