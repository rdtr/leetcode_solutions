package main

func generateParenthesis(n int) []string {
	if n == 0 {
		return []string{}
	}

	var res []string
	backtrack(n, 0, []byte{}, &res)
	return res
}

// backtrack does the actual parenthesis adding,
// leftCount means how many more left parenthesises should appear. This changes from 3 to 0.
// rightCount means how many right parenthesises should appear. This starts from 0 and
// incremented when leftCount is added, then finally this should be 0.
func backtrack(leftCount int, rightCount int, curBytes []byte, res *[]string) {
	// base case
	if leftCount == 0 && rightCount == 0 {
		*res = append(*res, string(curBytes))
		return
	}

	curLen := len(curBytes)
	if leftCount > 0 {
		newBytes := make([]byte, curLen+1)
		copy(newBytes[:curLen], curBytes)
		newBytes[curLen] = '('

		backtrack(leftCount-1, rightCount+1, newBytes, res)
	}
	if rightCount > 0 {
		newBytes := make([]byte, curLen+1)
		copy(newBytes[:curLen], curBytes)
		newBytes[curLen] = ')'

		backtrack(leftCount, rightCount-1, newBytes, res)
	}
}
