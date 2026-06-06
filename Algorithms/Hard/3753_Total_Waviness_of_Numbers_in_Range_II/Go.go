package main

import (
	"fmt"
)

func totalWaviness(num1 int64, num2 int64) int64 {
	type State struct {
		tight, lead, prev, curr int
		cnt, sum                int64
	}

	solve := func(num int64) int64 {
		if num < 100 {
			return 0
		}

		s := fmt.Sprintf("%d", num)
		n := len(s)
		currStates := []State{{1, 1, 10, 10, 1, 0}}
		for pos := 0; pos < n; pos++ {
			limit := int(s[pos] - '0')
			cnt := [2][2][11][11]int64{}
			sum := [2][2][11][11]int64{}
			for _, st := range currStates {
				maxDigit := limit
				if st.tight == 0 {
					maxDigit = 9
				}

				for digit := 0; digit <= maxDigit; digit++ {
					newLead, newPrev, newCurr := 0, st.curr, digit
					if st.lead == 1 && digit == 0 {
						newLead = 1
						newCurr = 10
					}

					newTight, add := 0, int64(0)
					if st.tight == 1 && digit == maxDigit {
						newTight = 1
					}

					if newLead == 0 && st.prev != 10 && st.curr != 10 {
						if (st.prev < st.curr && st.curr > digit) || (st.prev > st.curr && st.curr < digit) {
							add = st.cnt
						}
					}

					cnt[newTight][newLead][newPrev][newCurr] += st.cnt
					sum[newTight][newLead][newPrev][newCurr] += st.sum + add
				}
			}

			nextStates := []State{}
			for tight := 0; tight <= 1; tight++ {
				for lead := 0; lead < 2; lead++ {
					for prev := 0; prev <= 10; prev++ {
						for curr := 0; curr <= 10; curr++ {
							if cnt[tight][lead][prev][curr] != 0 {
								nextStates = append(nextStates, State{tight, lead, prev, curr, cnt[tight][lead][prev][curr], sum[tight][lead][prev][curr]})
							}
						}
					}
				}
			}

			currStates = nextStates
		}

		ans := int64(0)
		for _, st := range currStates {
			ans += st.sum
		}

		return ans
	}

	return solve(num2) - solve(num1-1)
}
