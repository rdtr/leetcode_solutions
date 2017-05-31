func canCompleteCircuit(gas []int, cost []int) int {
	glen := len(gas)
	var start, amount int
LOOP:
	// loop to set a new start point
	for i := 0; i < glen; {
		start, amount = i, 0
		// loop to check if we can complete a cycle from start to end
		for j := 0; j < glen; j++ {
			cur := (start + j) % glen
			if amount = amount + gas[cur] - cost[cur]; amount < 0 {
				if i+j >= glen {
					return -1 // all start points failed
				}
				i += j + 1 // skip the start point
				continue LOOP
			}
		}
		return start
	}
	return -1
}