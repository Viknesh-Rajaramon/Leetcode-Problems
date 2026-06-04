func totalWaviness(num1 int, num2 int) int {
    result := 0
    for num := num1; num <= num2; num++ {
        s := strconv.Itoa(num)
        for j := 1; j < len(s)-1; j++ {
            if (s[j-1] > s[j] && s[j] < s[j+1]) || (s[j-1] < s[j] && s[j] > s[j+1]) {
                result++
            }
        }
    }

    return result
}
