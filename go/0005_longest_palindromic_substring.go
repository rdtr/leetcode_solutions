package main

func longestPalindrome(s string) string {
	slen := len(s)
	var left, right int
	for i := 0; i < slen; i++ {
		l1, r1 := expandOdd(s, i)
		l2, r2 := expandEven(s, i)

		if r1-l1 >= right-left {
			left, right = l1, r1
		}
		if r2-l2 >= right-left {
			left, right = l2, r2
		}
	}
	return s[left : right+1]
}

func expandOdd(s string, i int) (left, right int) {
	for interval := 0; i-interval >= 0 && i+interval < len(s); interval++ {
		if s[i-interval] != s[i+interval] {
			break
		}
		left, right = i-interval, i+interval
	}
	return
}

func expandEven(s string, i int) (left, right int) {
	for interval := 0; i-interval >= 0 && i+interval+1 < len(s); interval++ {
		if s[i-interval] != s[i+interval+1] {
			break
		}
		left, right = i-interval, i+interval+1
	}
	return
}
