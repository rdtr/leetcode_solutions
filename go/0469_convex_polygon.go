func isConvex(points [][]int) bool {
	plen, negative, positive := len(points), false, false
	for i := 0; i < len(points); i++ {
		cur, next, nextNext := points[i%plen], points[(i+1)%plen], points[(i+2)%plen]
		if compareSlope(cur, next, nextNext) < 0 {
			negative = true
		} else if compareSlope(cur, next, nextNext) > 0 {
			positive = true
		}
		if negative && positive {
			return false
		}
	}
	return true
}

func compareSlope(p1, p2, p3 []int) int {
	switch diff := (p2[1]-p1[1])*(p3[0]-p2[0]) - (p3[1]-p2[1])*(p2[0]-p1[0]); {
	case diff > 0:
		return 1
	case diff < 0:
		return -1
	}
	return 0
}