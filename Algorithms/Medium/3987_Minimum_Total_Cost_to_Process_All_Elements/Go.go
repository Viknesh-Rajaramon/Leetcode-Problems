package main

func minimumCost(nums []int, k int) int {
	result, resources, mod := 0, k, 1000000007
	for _, num := range nums {
		if resources < num {
			i := (num - resources + k - 1) / k
			resources += i * k
			result += i
		}

		resources -= num
	}

	return (((result % mod) * ((result + 1) % mod) / 2) % mod)
}
