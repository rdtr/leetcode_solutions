func kEmptySlots(flowers []int, k int) int {
	bit, isBloom := make(BIT, len(flowers)+1), make([]int, len(flowers))
	for i, f := range flowers {
		f-- // adjut to (0..N)
		add(bit, f, 1)
		isBloom[f] = 1
		if (f-k-1 >= 0 && isBloom[f-k-1] == 1 && sum(bit, f-1)-sum(bit, f-k-1) == 0) ||
			(f+k+1 < len(flowers) && isBloom[f+k+1] == 1 && sum(bit, f+k)-sum(bit, f) == 0) {
			return i + 1
		}
	}
	return -1
}

type BIT []int

func add(bit BIT, index, value int) {
	for index = index + 1; index < len(bit); {
		bit[index] += value
		index += index & -index
	}
}

func sum(bit BIT, index int) (sum int) {
	for index = index + 1; index > 0; {
		sum += bit[index]
		index -= index & -index
	}
	return sum
}