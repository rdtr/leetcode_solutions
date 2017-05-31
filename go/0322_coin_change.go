func coinChange(coins []int, amount int) int {
	// corner case, amount = 0
	if amount == 0 {
		return 0
	}

	// visited memorized calculated sum-amount
	queue, visited := []int{0}, make(map[int]bool)
	level, sum := 0, 0
	for len(queue) > 0 {
		qlen := len(queue)
		for i := 0; i < qlen; i++ {
			cur := queue[0]
			for j := 0; j < len(coins); j++ {
				sum = cur + coins[j]
				if cur+coins[j] == amount {
					return level + 1
				}
				if cur+coins[j] > amount {
					continue
				}
				if _, ok := visited[sum]; ok {
					continue
				}
				queue, visited[sum] = append(queue, sum), true
			}
			queue = queue[1:]
		}
		level++
	}
	return -1
}