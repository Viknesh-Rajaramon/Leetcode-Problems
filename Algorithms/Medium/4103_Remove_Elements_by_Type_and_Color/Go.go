package main

func canRemoveAll(types []int, colors []int, groupSize []int) bool {
	stack := make([][]int, 0)
	for i, t := range types {
		if len(stack) > 0 && stack[len(stack)-1][0] == t && stack[len(stack)-1][1] == colors[i] {
			stack[len(stack)-1][2]++
		} else {
			stack = append(stack, []int{t, colors[i], 1})
		}

		if stack[len(stack)-1][2] == groupSize[t] {
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}
