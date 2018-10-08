package main

import "sort"

func carFleet(target int, position []int, speed []int) int {
	carlen := len(position)
	if carlen <= 1 {
		return carlen
	}

	cars := make([]*Car, carlen)
	for i := 0; i < carlen; i++ {
		cars[i] = &Car{Position: position[i], Speed: speed[i]}
	}

	sort.Slice(cars, func(i, j int) bool {
		if cars[i].Position >= cars[j].Position {
			return true
		}
		return false
	})

	fleet := 1
	carInFront := cars[0]
	for i := 1; i < carlen; i++ {
		if float32(target-carInFront.Position)/float32(carInFront.Speed) <
			float32(target-cars[i].Position)/float32(cars[i].Speed) {
			fleet++
			carInFront = cars[i]
		}
	}
	return fleet
}

type Car struct {
	Position int
	Speed    int
}
