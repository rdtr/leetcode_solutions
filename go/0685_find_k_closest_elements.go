func findClosestElements(arr []int, k int, x int) []int {
	base := findLeft(arr, x)
	left, right := base, base+1

	alen := len(arr)

	var res []int
	for len(res) < k {
		if right > alen-1 {
			res = append([]int{arr[left]}, res...)
			left--
		} else if left < 0 {
			res = append(res, arr[right])
			right++
		} else {
			if absDiff(x, arr[right]) < absDiff(x, arr[left]) {
				res = append(res, arr[right])
				right++
			} else {
				res = append([]int{arr[left]}, res...)
				left--
			}
		}
	}
	return res
}

func findLeft(arr []int, x int) int {
	l, r := 0, len(arr)-1
	for r-l > 1 {
		mid := l + (r-l)/2
		if arr[mid] > x {
			r = mid - 1
		} else if arr[mid] == x {
			r = mid
		} else {
			l = mid
		}
	}
	return l
}

func absDiff(x, y int) int {
	diff := x - y
	if diff < 0 {
		return -diff
	}
	return diff
}