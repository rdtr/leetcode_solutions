func trap(height []int) int {
	hlen := len(height)
	if hlen < 3 {
		return 0
	}
	highestLeft, highestRight := make([]int, hlen), make([]int, hlen)

	// i = 0
	highestLeft[0], highestRight[hlen-1] = 0, 0
	// i = 1
	highestLeft[1], highestRight[hlen-2] = height[0], height[hlen-1]
	maxl, maxr := highestLeft[1], highestRight[hlen-2]

	j := 0
	for i := 2; i < hlen; i++ {
		j = hlen - i - 1
		maxl, maxr = max(height[i-1], maxl), max(height[j+1], maxr)
		highestLeft[i], highestRight[j] = maxl, maxr
	}

	water := 0
	for i := 0; i < hlen; i++ {
		if highestLeft[i] > highestRight[i] {
			water += max(highestRight[i]-height[i], 0)
		} else if highestLeft[i] <= highestRight[i] {
			water += max(highestLeft[i]-height[i], 0)
		}
	}
	return water
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}