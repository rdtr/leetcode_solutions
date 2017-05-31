package main

func grayCode(n int) []int {
	if n == 0 {
		return []int{0}
	}

	res := []int{0, 1}
	base := 2
	for i := 1; i < n; i++ {
		rlen := len(res)
		for j := rlen - 1; j >= 0; j-- {
			res = append(res, res[j]+base)
		}
		base = base * 2
	}
	return res
}
