func check(nums []int) bool {
    n := len(nums)
    count := 0
    if nums[0] < nums[n-1] {
        count++
    }
    
    for i := 0; i < n-1; i++ {
        if nums[i] > nums[i+1] {
            count++
        }
    }
    
    return count <= 1
}
