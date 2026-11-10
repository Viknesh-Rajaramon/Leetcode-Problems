package main

func climbStairs(n int, costs []int) int {
	result, step_1, step_0 := 0, 0, 0
	for _, cost := range costs {
		step_0, step_1, result = step_1, result, cost+min(step_0+9, step_1+4, result+1)
	}

	return result
}
