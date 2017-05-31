func sortedArrayToBST(nums []int) *TreeNode {
	nlen := len(nums)
	if nlen == 0 {
		return nil
	}

	mid := nlen / 2
	root := &TreeNode{Val: nums[mid]}
	buildTree(0, mid-1, nums, root, true)
	buildTree(mid+1, nlen-1, nums, root, false)
	return root
}

func buildTree(left int, right int, nums []int, parent *TreeNode, isLeft bool) {
	if left > right {
		return
	}

	mid := left + (right-left)/2
	var nextParent *TreeNode
	if isLeft {
		parent.Left = &TreeNode{Val: nums[mid]}
		nextParent = parent.Left
	} else {
		parent.Right = &TreeNode{Val: nums[mid]}
		nextParent = parent.Right
	}
	buildTree(left, mid-1, nums, nextParent, true)
	buildTree(mid+1, right, nums, nextParent, false)
}