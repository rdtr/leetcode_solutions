package main

func generateParenthesis(n int) []string {
	if n == 0 {
		return []string{}
	}

	leftRemain, rightRemain := n-1, n
	cur := []byte{'('}
	var res []string
	doGenerateParenthesis(leftRemain, rightRemain, cur, &res)
	return res
}

func doGenerateParenthesis(leftRemain, rightRemain int, cur []byte, res *[]string) {
	if leftRemain == 0 && rightRemain == 0 {
		*res = append(*res, string(cur))
		return
	}

	if leftRemain > 0 {
		doGenerateParenthesis(leftRemain-1, rightRemain, append(cur, '('), res)
	}
	if rightRemain > leftRemain {
		doGenerateParenthesis(leftRemain, rightRemain-1, append(cur, ')'), res)
	}
}
