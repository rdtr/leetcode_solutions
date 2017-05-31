package main

func plusOne(digits []int) []int {
	dlen := len(digits)
	for i := dlen - 1; i >= 0; i-- {
		sum := digits[i] + 1
		if sum < 10 {
			digits[i] = sum
			break
		}

		digits[i] = sum - 10

		if i == 0 {
			return append([]int{1}, digits...)
		}

	}
	return digits
}
