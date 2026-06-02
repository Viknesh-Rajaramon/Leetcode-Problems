func minimumSwaps(nums []int) int {
    result, left, right := 0, 0, len(nums)-1
    for left < right {
        for right >= 0 && nums[right] == 0 {
            right -= 1
        }

        if right < 0 || right < left {
            break
        }

        if nums[left] == 0 {
            result += 1
            right -= 1
        }

        left += 1
    }

    return result
}
