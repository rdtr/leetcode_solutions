import "sort"

func countSmaller(nums []int) []int {
	nlen := len(nums)

	sorted := make([]int, nlen)
	copy(sorted, nums)
	sort.Ints(sorted)

	mp := make(map[int]int)
	index := 0
	for i := range sorted {
		if _, ok := mp[sorted[i]]; !ok {
			mp[sorted[i]] = index
			index++
		}
	}

	bit := make(BIT, len(mp)+1)

	res := make([]int, nlen)
	for i := nlen - 1; i >= 0; i-- {
		res[i] = sum(bit, mp[nums[i]]-1)
		add(bit, mp[nums[i]], 1)
	}
	return res
}

type BIT []int

func add(b BIT, index int, value int) {
	i := index + 1
	for i < len(b) {
		b[i] += value
		i += i & (-i)
	}
}

func sum(b BIT, index int) int {
	sum := 0
	for i := index + 1; i > 0; i = i - i&(-i) {
		sum += b[i]
	}
	return sum
}