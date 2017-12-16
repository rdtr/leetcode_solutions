/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findLeaves(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	var res [][]int
	count := 0
	helper(root, &res, &count)
	return res
}

func helper(parent *TreeNode, res *[][]int, count *int) {
	if parent.Left == nil && parent.Right == nil {
		addNode(res, parent, 0)
		return
	}

	lc, rc := *count, *count
	if parent.Left != nil {
		helper(parent.Left, res, &lc)
	}

	if parent.Right != nil {
		helper(parent.Right, res, &rc)
	}

	*count = max(lc, rc) + 1
	addNode(res, parent, *count)
}

func addNode(res *[][]int, node *TreeNode, count int) {
	if len(*res) > count {
		(*res)[count] = append((*res)[count], node.Val)
		return
	}
	*res = append(*res, []int{node.Val})
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}