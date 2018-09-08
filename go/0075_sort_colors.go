package main

func sortColors(nums []int) {
	if len(nums) == 0 {
		return
	}

	red, blue := 0, len(nums)-1
	i := 0
	for i <= blue {
		switch nums[i] {
		case 0:
			nums[i], nums[red] = nums[red], nums[i]
			red++
			i++
		case 1:
			i++
		case 2:
			nums[i], nums[blue] = nums[blue], nums[i]
			blue--
		}
	}
}
