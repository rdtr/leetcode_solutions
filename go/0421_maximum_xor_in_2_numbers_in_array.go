func findMaximumXOR(nums []int) int {
	root := NewNode()

	// build trie
	for _, num := range nums {
		cur := root
		for i := 31; i >= 0; i-- {
			flag := (num >> uint(i)) & 1
			if cur.Children[flag] == nil {
				cur.Children[flag] = NewNode()
			}
			cur = cur.Children[flag]
		}
	}

	// search maximum
	max := 0
	for _, num := range nums {
		cur, val := root, 0
		for i := 31; i >= 0; i-- {
			flag := (num >> uint(i)) & 1
			switch {
			case flag == 1 && cur.Children[0] != nil, flag == 0 && cur.Children[1] != nil:
				val += 1 << uint(i)
				cur = cur.Children[1 & ^flag] // just reversing flag
			default:
				cur = cur.Children[flag]
			}
		}
		if val > max {
			max = val
		}
	}
	return max
}

type TNode struct {
	Children [2]*TNode
}

func NewNode() *TNode {
	return &TNode{Children: [2]*TNode{nil, nil}}
}