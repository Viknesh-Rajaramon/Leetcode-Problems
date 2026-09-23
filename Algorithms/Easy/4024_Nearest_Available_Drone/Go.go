package main

import (
	"math"
)

func nearestDrone(drones [][]int, target []int) int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	result, min_dist := -1, math.MaxInt
	for i := range drones {
		dist := abs(drones[i][0]-target[0]) + abs(drones[i][1]-target[1])
		if dist <= drones[i][2] && dist < min_dist {
			result, min_dist = i, dist
		}
	}

	return result
}
