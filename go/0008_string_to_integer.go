package main

import "math"

func myAtoi(str string) int {
	if str == "" {
		return 0
	}

	i := 0
	for str[i] == ' ' {
		i++
	}

	positive := true
	if str[i] == '+' {
		i++
	} else if str[i] == '-' {
		i++
		positive = false
	}

	var res int
	for ; i < len(str); i++ {
		diff := int(str[i] - '0')
		if diff < 0 || diff > 9 {
			break
		}

		if positive {
			if res > (math.MaxInt32-diff)/10 {
				return math.MaxInt32
			}
			res = res*10 + diff
			continue
		}
		if res < (math.MinInt32+diff)/10 {
			return math.MinInt32
		}
		res = res*10 - diff
	}
	return res
}
