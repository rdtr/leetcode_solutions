func rotate(matrix [][]int) {
	m := len(matrix)
	top, bottom, right, left := 0, m-1, m-1, 0
	for top < bottom {
		num := right - left + 1
		for i := 0; i < num-1; i++ {
			tmp := matrix[top][left+i]
			matrix[top][left+i] = matrix[bottom-i][left]
			matrix[bottom-i][left] = matrix[bottom][right-i]
			matrix[bottom][right-i] = matrix[top+i][right]
			matrix[top+i][right] = tmp
		}
		top, bottom, right, left = top+1, bottom-1, right-1, left+1
	}
}