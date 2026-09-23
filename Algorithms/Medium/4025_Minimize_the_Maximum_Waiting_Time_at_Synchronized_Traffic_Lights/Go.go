package main

import (
	"math"
)

func minPenalty(period int, lights []int, arrivalTime []int) int {
	result, max_light := math.MaxInt, 0
	for _, light := range lights {
		max_light = max(max_light, light)
	}

	for _, time := range arrivalTime {
		r := time % period
		if r >= max_light {
			result = min(result, r)
		}
	}

	if result == math.MaxInt {
		return 0
	}

	return period - result
}
