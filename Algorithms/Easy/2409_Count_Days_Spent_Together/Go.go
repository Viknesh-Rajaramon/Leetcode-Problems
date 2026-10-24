package main

func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
	f := func(s string) int {
		month, day := int((s[0]-'0')*10+s[1]-'0'), int((s[3]-'0')*10+s[4]-'0')
		return (275*month)/9 - 2*((month+9)/12) + day - 30
	}

	return max(0, min(f(leaveAlice), f(leaveBob))-max(f(arriveAlice), f(arriveBob))+1)
}
