package main

func minimumCost(cost1 int, cost2 int, costBoth int, need1 int, need2 int) int64 {
	cost_a := int64(need1*cost1 + need2*cost2)
	cost_b := int64(min(need1, need2) * (costBoth - cost1 - cost2))
	cost_c := int64(max(need1, need2) * costBoth)
	return min(cost_a+min(int64(0), cost_b), cost_c)
}
