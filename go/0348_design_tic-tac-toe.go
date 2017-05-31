type TicTacToe struct {
	N     int
	Rows  [][2]int
	Cols  [][2]int
	Diags [][2]int
}

/** Initialize your data structure here. */
func Constructor(n int) TicTacToe {
	ttt := TicTacToe{}
	ttt.N = n
	ttt.Rows = make([][2]int, n)
	ttt.Cols = make([][2]int, n)
	ttt.Diags = make([][2]int, 2)
	return ttt
}

/** Player {player} makes a move at ({row}, {col}).
  @param row The row of the board.
  @param col The column of the board.
  @param player The player, can be either 1 or 2.
  @return The current winning condition, can be either:
          0: No one wins.
          1: Player 1 wins.
          2: Player 2 wins. */
func (this *TicTacToe) Move(row int, col int, player int) int {
	p := player - 1
	if this.Rows[row][p] = this.Rows[row][p] + 1; this.Rows[row][p] == this.N {
		return player
	}
	if this.Cols[col][p] = this.Cols[col][p] + 1; this.Cols[col][p] == this.N {
		return player
	}
	if row == col {
		if this.Diags[0][p] = this.Diags[0][p] + 1; this.Diags[0][p] == this.N {
			return player
		}
	}
	if row == this.N-col-1 {
		if this.Diags[1][p] = this.Diags[1][p] + 1; this.Diags[1][p] == this.N {
			return player
		}
	}
	return 0
}