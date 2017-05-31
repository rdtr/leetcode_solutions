func searchMatrix(matrix [][]int, target int) bool {
	ylen := len(matrix)
	if ylen == 0 {
		return false
	}
	xlen := len(matrix[0])

	top, bottom, left, right := 0, ylen-1, 0, xlen-1
	res := false
	doSearch(&res, matrix, target, top, bottom, left, right)
	return res
}

func doSearch(res *bool, matrix [][]int, target int, top, bottom, left, right int) {
	if *res || bottom < top || right < left {
		return
	}
	midy, midx := top+(bottom-top)/2, left+(right-left)/2
	mid := matrix[midy][midx]
	if mid == target {
		*res = true
		return
	}

	if mid < target {
		doSearch(res, matrix, target, top, midy, midx+1, right)
		doSearch(res, matrix, target, top+1, bottom, midx+1, right)
		doSearch(res, matrix, target, top+1, bottom, left, midx)
		return
	}
	doSearch(res, matrix, target, top, midy-1, left, midx-1)
	doSearch(res, matrix, target, top, midy-1, midx, right)
	doSearch(res, matrix, target, midy, bottom, left, midx-1)
}

/////////////////////////////////////////////////////////

func searchMatrix(matrix [][]int, target int) bool {
	ylen := len(matrix)
	if ylen == 0 {
		return false
	}
	xlen := len(matrix[0])
	if xlen == 0 {
		return false
	}

	x, y := xlen-1, 0
	current := matrix[y][x]

	stop := false
	for {
		switch {
		case current < target:
			y++
			stop = (y > ylen-1)
		case current > target:
			x--
			stop = (x < 0)
		default:
			return true
		}
		if stop {
			break
		}
		current = matrix[y][x]
	}
	return false
}