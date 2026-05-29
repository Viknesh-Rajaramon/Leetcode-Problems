func minElement(nums []int) int {
    result := 9+9+9+9
    for _, num := range nums {
        sum := 0
		for num > 0 {
			sum += num%10
            num /= 10
		}

		result = min(result, sum)
    }

    return result
}
