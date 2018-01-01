import "sort"

func reconstructQueue(people [][]int) [][]int {
	sort.Sort(ByHeightAndRank(people))
	res := make([][]int, 0)
	for i := 0; i < len(people); i++ {
		insert(&res, people[i], people[i][1])
	}
	return res
}

func insert(sli *[][]int, elem []int, index int) {
	*sli = append(*sli, []int{}) // insert dummy
	copy((*sli)[index+1:], (*sli)[index:])
	(*sli)[index] = elem
}

type ByHeightAndRank [][]int

func (b ByHeightAndRank) Len() int {
	return len(b)
}

func (b ByHeightAndRank) Less(i, j int) bool {
	if b[i][0] > b[j][0] {
		return true
	} else if b[i][0] < b[j][0] {
		return false
	}
	return b[i][1] < b[j][1]
}

func (b ByHeightAndRank) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
}