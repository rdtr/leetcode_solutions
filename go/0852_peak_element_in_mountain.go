func peakIndexInMountainArray(A []int) int {
	low, high := 0, len(A)-1
	mid := low + (high-low)/2
	for low < high {
		if A[mid-1] < A[mid] && A[mid] > A[mid+1] {
			return mid
		}
		if A[mid-1] < A[mid] && A[mid] < A[mid+1] {
			low = mid
			mid = low + (high-low)/2
			continue
		}
		if A[mid-1] > A[mid] && A[mid] > A[mid+1] {
			high = mid
			mid = low + (high-low)/2
			continue
		}
		break
	}
	return -1
}