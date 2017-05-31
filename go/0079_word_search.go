func exist(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			p := board[i][j]
			if p == word[0] {
				res := false
				search(&res, i, j, m, n, board, word, 0)
				if res {
					return true
				}
			}
		}
	}
	return false
}

func search(res *bool, i, j, m, n int, board [][]byte, word string, currentIndex int) {
	var zeroByte byte
	if *res || word[currentIndex] != board[i][j] || board[i][j] == zeroByte {
		return
	}
	if currentIndex == len(word)-1 {
		*res = true
		return
	}

	nextIndex := currentIndex + 1
	tmp := board[i][j]
	board[i][j] = zeroByte
	if i > 0 {
		search(res, i-1, j, m, n, board, word, nextIndex)
	}
	if i < m-1 {
		search(res, i+1, j, m, n, board, word, nextIndex)
	}
	if j > 0 {
		search(res, i, j-1, m, n, board, word, nextIndex)
	}
	if j < n-1 {
		search(res, i, j+1, m, n, board, word, nextIndex)
	}
	board[i][j] = tmp
}