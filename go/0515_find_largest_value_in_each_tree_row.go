import "math"

func largestValues(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	q := []*TreeNode{root}
	var res []int

	for len(q) > 0 {
		qlen := len(q)
		max := math.MinInt32
		for i := 0; i < qlen; i++ {
			node := q[0]
			q = q[1:]

			if node.Val > max {
				max = node.Val
			}

			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
		res = append(res, max)
	}
	return res
}