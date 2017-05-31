package main

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	nodes := []*TreeNode{root}
	dfsRight(&nodes, root)

	res, count := true, 0
	dfsLeft(&res, &count, nodes, root)
	return res
}

func dfsRight(nodes *[]*TreeNode, root *TreeNode) {
	if root == nil {
		return
	}
	*nodes = append(*nodes, root.Right)
	dfsRight(nodes, root.Right)
	*nodes = append(*nodes, root.Left)
	dfsRight(nodes, root.Left)
}

func dfsLeft(res *bool, count *int, nodes []*TreeNode, root *TreeNode) {
	if root == nil {
		return
	}

	*count = *count + 1
	node, left := nodes[*count], root.Left
	if (node == nil && left == nil) || (node != nil && left != nil && node.Val == left.Val) {
		dfsLeft(res, count, nodes, root.Left)
	} else {
		*res = false
		return
	}

	*count = *count + 1
	node, right := nodes[*count], root.Right
	if (node == nil && right == nil) || (node != nil && right != nil && node.Val == right.Val) {
		dfsLeft(res, count, nodes, root.Right)
	} else {
		*res = false
		return
	}
}
