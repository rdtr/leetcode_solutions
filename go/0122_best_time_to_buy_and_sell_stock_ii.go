func maxProfit(prices []int) int {
	profit, sell := 0, false

	for i := 0; i < len(prices); i++ {
		if sell {
			profit, sell = profit+prices[i]-prices[i-1], false
		}
		sell = i < len(prices)-1 && prices[i] < prices[i+1]
	}
	return profit
}