package main

func minMaxWaitingTime(demand []int, fuel []int) int {
	n := len(demand)
	type State struct {
		f0 int
		f1 int
		t0 int
		t1 int
	}

	check := func(wait_limit int) int {
		states, served := make(map[State]struct{}), 0
		states[State{fuel[0], fuel[1], 0, 0}] = struct{}{}
		for i := range n {
			nxt := make(map[State]struct{})
			for state := range states {
				f0, f1, t0, t1 := state.f0, state.f1, state.t0, state.t1
				if f0 >= demand[i] && t0 <= wait_limit {
					nxt[State{f0 - demand[i], f1, demand[i], max(0, t1-t0)}] = struct{}{}
				}

				if f1 >= demand[i] && t1 <= wait_limit {
					nxt[State{f0, f1 - demand[i], max(0, t0-t1), demand[i]}] = struct{}{}
				}
			}

			if len(nxt) == 0 {
				break
			}

			states = nxt
			served++
		}

		return served
	}

	mx := check(1e9)
	if mx == 0 {
		return -1
	}

	low, high := 0, 0
	for _, num := range demand {
		high += num
	}

	for low <= high {
		mid := (low + high) >> 1
		if check(mid) == mx {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return low
}
