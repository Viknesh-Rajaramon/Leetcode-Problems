package main

func shadowPairs(nums []int) int64 {
	result, total, stack := int64(0), int64(0), make([][]int64, 0)
	for _, n := range nums {
		num := int64(n)
		for len(stack) > 0 && num < stack[len(stack)-1][0] {
			total -= stack[len(stack)-1][1]
			stack = stack[:len(stack)-1]
		}

		if len(stack) > 0 {
			result += total
			if stack[len(stack)-1][0] == num {
				result -= stack[len(stack)-1][1]
				stack[len(stack)-1][1]++
			} else {
				stack = append(stack, []int64{num, 1})
			}
		} else {
			stack = append(stack, []int64{num, 1})
		}

		total++
	}

	return result
}
