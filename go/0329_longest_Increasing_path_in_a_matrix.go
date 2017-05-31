func longestIncreasingPath(matrix [][]int) int {
	mlen := len(matrix)
	if mlen == 0 {
		return 0
	}
	nlen := len(matrix[0])

	cache := make(map[P]int)

	res := 0
	for m := 0; m < mlen; m++ {
		for n := 0; n < nlen; n++ {
			if curRes := checkPath(m, n, matrix, cache); curRes > res {
				res = curRes
			}
		}
	}
	return res
}

func checkPath(m, n int, matrix [][]int, cache map[P]int) int {
	if cachePath, ok := cache[P{X: m, Y: n}]; ok {
		return cachePath
	}

	max := 0
	if m > 0 && matrix[m-1][n] > matrix[m][n] {
		if left := checkPath(m-1, n, matrix, cache); left > max {
			max = left
		}
	}
	if m < len(matrix)-1 && matrix[m+1][n] > matrix[m][n] {
		if right := checkPath(m+1, n, matrix, cache); right > max {
			max = right
		}
	}
	if n > 0 && matrix[m][n-1] > matrix[m][n] {
		if bottom := checkPath(m, n-1, matrix, cache); bottom > max {
			max = bottom
		}
	}
	if n < len(matrix[0])-1 && matrix[m][n+1] > matrix[m][n] {
		if top := checkPath(m, n+1, matrix, cache); top > max {
			max = top
		}
	}
	cache[P{X: m, Y: n}] = max + 1
	return max + 1
}

type P struct {
	X int
	Y int
}