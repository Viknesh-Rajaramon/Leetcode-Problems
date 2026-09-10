package main

func maxSlidingWindow(nums []int, k int) []int {
	result, q := make([]int, 0), make([]int, 0)
	for i, num := range nums {
		for len(q) > 0 && q[len(q)-1] < num {
			q = q[:len(q)-1]
		}

		q = append(q, num)
		if i >= k && nums[i-k] == q[0] {
			q = q[1:]
		}

		if i >= k-1 {
			result = append(result, q[0])
		}
	}

	return result
}
