package main

func sortPermutation(nums []int) int {
	result, flag := 0, false
	for i, num := range nums {
		if num == i {
			continue
		}

		if !flag {
			result = num
			flag = true
		} else {
			result &= num
		}
	}

	if flag {
		return result
	}

	return 0
}
