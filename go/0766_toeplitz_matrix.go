func isToeplitzMatrix(matrix [][]int) bool {
	mlen := len(matrix)
	if mlen == 0 {
		return false
	}
	nlen := len(matrix[0])

	for i := 0; i < mlen; i++ {
		for j := 0; j < nlen; j++ {
			if i != 0 && j != 0 {
				if matrix[i][j] != matrix[i-1][j-1] {
					return false
				}
			}
		}
	}
	return true
}