package main

func minOperations(nums []int) int {
	n, ind_0 := len(nums), 0
	for i := range nums {
		if nums[i] == 0 {
			ind_0 = i
			break
		}
	}

	result := true
	for i := ind_0; i < ind_0+n-1; i++ {
		if nums[i%n] >= nums[(i+1)%n] {
			result = false
			break
		}
	}

	if result {
		return min(ind_0, n+2-ind_0)
	}

	result = true
	for i := ind_0; i > ind_0-n+1; i-- {
		if nums[(n+i)%n] >= nums[(n+i-1)%n] {
			result = false
			break
		}
	}

	if result {
		return min(n-ind_0, 2+ind_0)
	}

	return -1
}
