func dailyTemperatures(temperatures []int) []int {
	tlen := len(temperatures)
	res := make([]int, tlen)
	if tlen == 0 {
		return res
	}

	var stack []int
	for i := tlen - 1; i >= 0; i-- {
		if i == tlen-1 {
			res[i] = 0
			stack = append(stack, i)
			continue
		}

		for len(stack) > 0 && temperatures[stack[len(stack)-1]] <= temperatures[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			res[i] = 0
		} else {
			res[i] = stack[len(stack)-1] - i
		}
		stack = append(stack, i)
	}
	return res
}