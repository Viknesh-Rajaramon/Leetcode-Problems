func leftRightDifference(nums []int) []int {
    result, left_sum, total_sum := make([]int, 0), 0, 0
    for _, num := range nums {
        total_sum += num
    }

    abs := func(num int) int {
        if num < 0 {
            return -num
        }

        return num
    }

    for _, num := range nums {
        left_sum += num
        result = append(result, abs(total_sum - left_sum))
        total_sum -= num
    }

    return result
}
