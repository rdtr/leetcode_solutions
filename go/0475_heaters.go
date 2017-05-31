import "sort"

func findRadius(houses []int, heaters []int) int {
	sort.Ints(houses)
	sort.Ints(heaters)

	hi := 0 // closest index of heater
	maxDist := 0
	for i := 0; i < len(houses); i++ {
		house := houses[i]
		for hi < len(heaters)-1 && dist(house, heaters[hi]) >= dist(house, heaters[hi+1]) {
			hi++
		}

		if curDist := dist(house, heaters[hi]); curDist > maxDist {
			maxDist = curDist
		}
	}
	return maxDist
}

func dist(a, b int) int {
	if d := a - b; d < 0 {
		return -d
	} else {
		return d
	}
}