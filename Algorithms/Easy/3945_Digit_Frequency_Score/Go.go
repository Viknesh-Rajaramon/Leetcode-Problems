func digitFrequencyScore(n int) int {
    result := 0
    for n > 0 {
        result += n%10
        n /= 10
    }

    return result
}
