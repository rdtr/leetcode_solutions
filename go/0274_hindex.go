func hIndex(citations []int) int {
	buckets := make([]int, len(citations)+1)
	for _, c := range citations {
		if c >= len(citations) {
			buckets[len(buckets)-1]++
			continue
		}
		buckets[c]++
	}

	sofar := 0
	for i := len(buckets) - 1; i >= 0; i-- {
		sofar += buckets[i]
		if sofar >= i {
			return i
		}
	}
	return 0
}