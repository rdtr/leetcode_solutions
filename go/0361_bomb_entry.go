func maxKilledEnemies(grid [][]byte) int {
	mlen := len(grid)
	if mlen == 0 {
		return 0
	}
	nlen := len(grid[0])

	// initialize memo array
	memo := make([][]*FD, mlen)
	for i := 0; i < mlen; i++ {
		tmp := make([]*FD, nlen)
		for j := 0; j < nlen; j++ {
			tmp[j] = &FD{}
		}
		memo[i] = tmp
	}

	// sweep from left to right, top to bottom
	for i := 0; i < mlen; i++ {
		for j := 0; j < nlen; j++ {
			// calculate left side enemies
			if j == 0 {
				memo[i][j].Left = 0
			} else {
				switch grid[i][j-1] {
				case 'W':
					memo[i][j].Left = 0
				case 'E':
					memo[i][j].Left = memo[i][j-1].Left + 1
				default:
					memo[i][j].Left = memo[i][j-1].Left
				}
			}

			// calculate upper side enemies
			if i == 0 {
				memo[i][j].Top = 0
			} else {
				switch grid[i-1][j] {
				case 'W':
					memo[i][j].Top = 0
				case 'E':
					memo[i][j].Top = memo[i-1][j].Top + 1
				default:
					memo[i][j].Top = memo[i-1][j].Top
				}
			}
		}
	}

	// sweep from bottom to top, right to left
	for i := mlen - 1; i >= 0; i-- {
		for j := nlen - 1; j >= 0; j-- {
			// calculate right side enemies
			if j == nlen-1 {
				memo[i][j].Right = 0
			} else {
				switch grid[i][j+1] {
				case 'W':
					memo[i][j].Right = 0
				case 'E':
					memo[i][j].Right = memo[i][j+1].Right + 1
				default:
					memo[i][j].Right = memo[i][j+1].Right
				}
			}

			// calculate bottom side enemies
			if i == mlen-1 {
				memo[i][j].Bottom = 0
			} else {
				switch grid[i+1][j] {
				case 'W':
					memo[i][j].Bottom = 0
				case 'E':
					memo[i][j].Bottom = memo[i+1][j].Bottom + 1
				default:
					memo[i][j].Bottom = memo[i+1][j].Bottom
				}
			}
		}
	}

	// calculate sum and return maximum
	res := 0
	for i := 0; i < mlen; i++ {
		for j := 0; j < nlen; j++ {
			if sum := memo[i][j].Left + memo[i][j].Right + memo[i][j].Top + memo[i][j].Bottom; sum > res {
				if grid[i][j] == '0' { // ignore the case like "EEE"
					res = sum
				}
			}
		}
	}
	return res
}

type FD struct {
	Left   int
	Right  int
	Top    int
	Bottom int
}