func solve(board [][]byte) {
	mlen := len(board)
	if mlen == 0 {
		return
	}
	nlen := len(board[0])

	for i := 0; i < mlen; i++ {
		for j := 0; j < nlen; j++ {
			if board[i][j] == 'O' && (i == 0 || i == mlen-1 || j == 0 || j == nlen-1) {
				fill(board, i, j, mlen, nlen)
			}
		}
	}

	for i := 0; i < mlen; i++ {
		for j := 0; j < nlen; j++ {
			if ch := board[i][j]; ch == 'S' {
				board[i][j] = 'O'
			} else if ch == 'O' {
				board[i][j] = 'X'
			}
		}
	}
}

func fill(board [][]byte, x, y int, mlen, nlen int) {
	board[x][y] = 'S'
	if x-1 >= 0 && board[x-1][y] == 'O' {
		fill(board, x-1, y, mlen, nlen)
	}
	if x+1 <= mlen-1 && board[x+1][y] == 'O' {
		fill(board, x+1, y, mlen, nlen)
	}
	if y-1 >= 0 && board[x][y-1] == 'O' {
		fill(board, x, y-1, mlen, nlen)
	}
	if y+1 <= nlen-1 && board[x][y+1] == 'O' {
		fill(board, x, y+1, mlen, nlen)
	}
}