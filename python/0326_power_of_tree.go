package main

import "strconv"

func isPowerOfThree(n int) bool {
	s := strconv.FormatInt(int64(n), 3)
	if s == "1" {
		return true
	}
	if s[0] != '1' {
		return false
	}

	for _, ch := range s[1:] {
		if ch != '0' {
			return false
		}
	}
	return true
}
