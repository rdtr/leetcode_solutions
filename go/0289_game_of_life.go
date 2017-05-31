func gameOfLife(board [][]int) {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if l := check(board, i, j); (l == 2 && board[i][j] == 1) || l == 3 {
				board[i][j] += 10
			}
		}
	}

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			board[i][j] /= 10
		}
	}
}

func check(board [][]int, i, j int) int {
	live := 0
	neighbors := [][2]int{
		[2]int{i - 1, j - 1},
		[2]int{i - 1, j},
		[2]int{i - 1, j + 1},
		[2]int{i, j - 1},
		[2]int{i, j + 1},
		[2]int{i + 1, j - 1},
		[2]int{i + 1, j},
		[2]int{i + 1, j + 1},
	}
	for _, neighbor := range neighbors {
		if x, y := neighbor[0], neighbor[1]; x >= 0 && y >= 0 && x < len(board) && y < len(board[0]) 
			&& board[x][y]%10 == 1 {
			live++
		}
	}
	return live
}