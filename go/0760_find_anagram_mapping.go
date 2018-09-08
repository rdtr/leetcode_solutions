func anagramMappings(A []int, B []int) []int {
	mapb := make(map[int]*MyNode)
	for i := 0; i < len(B); i++ {
		if head, ok := mapb[B[i]]; ok {
			mapb[B[i]] = &MyNode{Idx: i, Next: head}
			continue
		}
		mapb[B[i]] = &MyNode{Idx: i, Next: nil}
	}

	res := make([]int, len(A))
	for i := 0; i < len(A); i++ {
		node, _ := mapb[A[i]]
		res[i] = node.Idx
		mapb[A[i]] = node.Next
	}
	return res
}

type MyNode struct {
	Idx  int
	Next *MyNode
}
