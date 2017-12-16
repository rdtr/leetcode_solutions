func buildTree(preorder []int, inorder []int) *TreeNode {
	l := len(preorder)
	if l == 0 {
		return nil
	} else if l == 1 {
		return &TreeNode{Val: preorder[0]}
	}

	root := &TreeNode{Val: preorder[0]}
	stack := []*TreeNode{root}

	m := make(map[int]int)
	for i := 0; i < len(inorder); i++ {
		m[inorder[i]] = i
	}

	var pop *TreeNode
	for i := 1; i < len(preorder); i++ {
		if m[preorder[i]] < m[stack[len(stack)-1].Val] {
			pop = stack[len(stack)-1]
			pop.Left = &TreeNode{Val: preorder[i]}
			stack = append(stack, pop.Left)
			continue
		}

		pop = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for len(stack) > 0 && m[preorder[i]] > m[stack[len(stack)-1].Val] {
			pop = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		pop.Right = &TreeNode{Val: preorder[i]}
		stack = append(stack, pop.Right)
	}
	return root
}