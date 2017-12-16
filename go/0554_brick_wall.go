func leastBricks(wall [][]int) int {
	wlen := len(wall)
	if wlen == 0 {
		return 0
	}

	// get the width of row
	width := 0
	for i := 0; i < len(wall[0]); i++ {
		width += wall[0][i]
	}

	// store count of borders per index in map
	edgeMap := make(map[int]int)

	min := wlen
	for i := 0; i < wlen; i++ {
		w := wall[i]

		x := 0
		for j := 0; j < len(w); j++ {
			x += w[j]
			if x == width {
				break
			}

			var bricks int
			if cnt, ok := edgeMap[x]; ok {
				edgeMap[x] = cnt + 1
				bricks = wlen - edgeMap[x]
			} else {
				edgeMap[x] = 1
				bricks = wlen - 1
			}

			if bricks < min {
				min = bricks
			}
		}
	}
	return min
}