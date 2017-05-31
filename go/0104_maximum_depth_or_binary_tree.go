package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	que := []*TreeNode{root}
	depth := 1
	start, end := 0, 1

	for {
		numOfChildren := 0
		for i := start; i < end; i++ {
			node := que[i]
			if node.Left != nil {
				que = append(que, node.Left)
				numOfChildren++
			}
			if node.Right != nil {
				que = append(que, node.Right)
				numOfChildren++
			}
		}
		if numOfChildren == 0 {
			break
		}

		depth++
		start = end
		end = end + numOfChildren
	}

	return depth
}
