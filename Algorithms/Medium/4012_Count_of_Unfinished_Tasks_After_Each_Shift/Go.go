package main

func countTasks(tasks []int, shifts []int) []int {
	bisect_right := func(arr []int, x int) int {
		low, high := 0, len(arr)-1
		for low <= high {
			mid := (low + high) >> 1
			if arr[mid] <= x {
				low = mid + 1
			} else {
				high = mid - 1
			}
		}

		return low
	}

	n := len(tasks)
	for i := range n - 1 {
		tasks[i+1] += tasks[i]
	}

	result, total, carry := make([]int, 0), tasks[n-1], 0
	for _, shift := range shifts {
		carry += shift
		if carry >= total {
			result = append(result, 0)
			carry = 0
		} else {
			result = append(result, n-bisect_right(tasks, carry))
		}
	}

	return result
}
