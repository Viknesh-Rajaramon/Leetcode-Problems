func findMin(nums []int) int {
    low, high := 0, len(nums)-1
    for low < high {
        mid := (low+high)/2
        if nums[mid] < nums[high] {
            high = mid
        } else if nums[mid] > nums[high] {
            low = mid+1
        } else {
            high -= 1
        }
    }

    return nums[low]
}
