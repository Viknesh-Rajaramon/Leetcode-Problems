package main

type BusBooking struct {
	cost       map[string]int
	total_time int
	min_time   int
}

func Constructor(n int) BusBooking {
	return BusBooking{
		cost:       make(map[string]int),
		total_time: 0,
		min_time:   0,
	}
}

func (this *BusBooking) Toggle(seat string) {
	if _, ok := this.cost[seat]; ok {
		this.total_time -= this.cost[seat]
		delete(this.cost, seat)
		this.min_time--
		return
	}

	c := 1
	if seat[0] == 'A' || seat[0] == 'D' {
		middle := 'C'
		if seat[0] == 'A' {
			middle = 'B'
		}

		if _, ok := this.cost[string(middle)+seat[1:]]; ok {
			c = 3
		}
	}

	this.cost[seat] = c
	this.total_time += c
	this.min_time++
}

func (this *BusBooking) GetTotalTime() int {
	return this.total_time
}

func (this *BusBooking) GetMinTime() int {
	return this.min_time
}

/**
 * Your BusBooking object will be instantiated and called as such:
 * obj := Constructor(n);
 * obj.Toggle(seat);
 * param_2 := obj.GetTotalTime();
 * param_3 := obj.GetMinTime();
 */
