package main

func stoneGameIII(stoneValue []int) string {
	s1, s2, s3, tot := 0, 0, 0, 0
	for i := len(stoneValue) - 1; i >= 0; i-- {
		tot += stoneValue[i]
		s1, s2, s3 = tot-min(s1, s2, s3), s1, s2
	}

	if 2*s1 > tot {
		return "Alice"
	} else if 2*s1 < tot {
		return "Bob"
	}

	return "Tie"
}
