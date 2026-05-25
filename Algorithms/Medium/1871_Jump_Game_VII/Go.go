func canReach(s string, minJump int, maxJump int) bool {
    n := len(s)
    result := make([]bool, n)
    pre := make([]int, n)
    for i := 0; i < minJump; i++ {
        pre[i] = 1
    }

    for i := minJump; i < n; i++ {
        left := i-maxJump
        if s[i] == '0' {
            total := pre[i-minJump]
            if left > 0 {
                total -= pre[left-1]
            }
            result[i] = bool(total != 0)
        }

        pre[i] = pre[i-1]
        if result[i] {
            pre[i] += 1
        }
    }

    return result[n-1]
}
