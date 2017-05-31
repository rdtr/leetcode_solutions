func change(amount int, coins []int) int {
	if amount == 0 {
		return 1
	} else if len(coins) == 0 {
		return 0
	} else if len(coins) == 1 {
		if amount%coins[0] == 0 {
			return 1
		}
		return 0
	}

	visited := make(map[Key]int)
	return doChange(amount, coins, visited)
}

func doChange(amount int, coins []int, visited map[Key]int) int {
	clen := len(coins)

	if amount == 0 {
		return 1
	} else if clen == 0 {
		return 0
	} else if clen == 1 {
		if amount%coins[0] == 0 {
			return 1
		}
		return 0
	}

	if ways, ok := visited[Key{Amount: amount, CoinLen: clen}]; ok {
		return ways
	}

	coin := coins[0]
	ways := 0
	for i := 0; i*coin <= amount; i++ {
		ways += doChange(amount-i*coin, coins[1:], visited)
	}

	visited[Key{Amount: amount, CoinLen: clen}] = ways
	return ways
}

// Key for visited map
type Key struct {
	Amount  int
	CoinLen int
}