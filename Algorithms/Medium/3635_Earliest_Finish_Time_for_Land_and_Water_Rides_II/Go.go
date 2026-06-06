package main

import (
	"math"
)

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	solve := func(firstStart, firstDur, secondStart, secondDur []int) int {
		result, end := math.MaxInt, math.MaxInt
		for i := range firstStart {
			end = min(end, firstStart[i]+firstDur[i])
		}

		for i := range secondStart {
			result = min(result, max(secondStart[i], end)+secondDur[i])
		}

		return result
	}

	return min(
		solve(landStartTime, landDuration, waterStartTime, waterDuration),
		solve(waterStartTime, waterDuration, landStartTime, landDuration),
	)
}
