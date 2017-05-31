func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return []int{}
	}

	var res []int
	top, bottom, left, right := 0, len(matrix)-1, 0, len(matrix[0])-1
	point := []int{0, 0}

	for {
		// move to right
		for i := point[1]; i <= right; i++ {
			res = append(res, matrix[point[0]][i])
		}
		if point[0] >= bottom {
			break
		}
		top, point[0], point[1] = top+1, point[0]+1, right

		// move to bottom
		for i := point[0]; i <= bottom; i++ {
			res = append(res, matrix[i][point[1]])
		}
		if point[1] <= left {
			break
		}
		right, point[0], point[1] = right-1, bottom, point[1]-1

		// move to left
		for i := point[1]; i >= left; i-- {
			res = append(res, matrix[point[0]][i])
		}
		if point[0] <= top {
			break
		}
		bottom, point[0], point[1] = bottom-1, point[0]-1, left

		// move to top
		for i := point[0]; i >= top; i-- {
			res = append(res, matrix[i][point[1]])
		}
		if point[1] >= right {
			break
		}
		left, point[0], point[1] = left+1, top, point[1]+1
	}
	return res
}