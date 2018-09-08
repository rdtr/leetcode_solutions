package main

func longestUnivaluePath(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	doLongestUnivaluePath(root, &res)
	return res
}

func doLongestUnivaluePath(node *TreeNode, res *int) int {
	switch {
	case node.Left == nil && node.Right == nil:
		return 0
	case node.Left != nil && node.Right == nil:
		h := doLongestUnivaluePath(node.Left, res)
		if node.Val == node.Left.Val {
			*res = max(*res, h+1)
			return h + 1
		}
		return 0
	case node.Left == nil && node.Right != nil:
		h := doLongestUnivaluePath(node.Right, res)
		if node.Val == node.Right.Val {
			*res = max(*res, h+1)
			return h + 1
		}
		return 0
	default:
		hl := doLongestUnivaluePath(node.Left, res)
		hr := doLongestUnivaluePath(node.Right, res)
		switch {
		case node.Val == node.Left.Val && node.Val == node.Right.Val:
			*res = max(*res, hl+hr+2)
			return max(hl, hr) + 1
		case node.Val != node.Left.Val && node.Val == node.Right.Val:
			*res = max(*res, hr+1)
			return hr + 1
		case node.Val == node.Left.Val && node.Val != node.Right.Val:
			*res = max(*res, hl+1)
			return hl + 1
		default:
			return 0
		}
	}
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}
