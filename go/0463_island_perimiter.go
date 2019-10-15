func islandPerimeter(grid [][]int) int {
	mlen := len(grid)
	if mlen == 0 {
		return 0
	}
	nlen := len(grid[0])

	perimiter := 0
	for i := 0; i < mlen; i++ {
		for j := 0; j < nlen; j++ {
			if grid[i][j] == 1 {
				tmp := 4
				if i > 0 && grid[i-1][j] == 1 {
					tmp--
				}
				if i < mlen-1 && grid[i+1][j] == 1 {
					tmp--
				}
				if j > 0 && grid[i][j-1] == 1 {
					tmp--
				}
				if j < nlen-1 && grid[i][j+1] == 1 {
					tmp--
				}
				perimiter += tmp
			}
		}
	}
	return perimiter
}