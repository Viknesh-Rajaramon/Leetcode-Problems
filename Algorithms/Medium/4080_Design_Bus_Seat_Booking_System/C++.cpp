class BusBooking {
private:
    unordered_map<string, int> cost;
    int total_time = 0;
    int min_time = 0;

public:
    BusBooking(int n) {
        
    }
    
    void toggle(string seat) {
        if (cost.count(seat)) {
            total_time -= cost[seat];
            cost.erase(seat);
            --min_time;
            return;
        }

        int c = 1;
        if (seat[0] == 'A' || seat[0] == 'D') {
            char middle = seat[0] == 'A' ? 'B' : 'C';
            if (cost.count(string(1, middle) + seat.substr(1)))
                c = 3;
        }
        
        cost[seat] = c;
        total_time += c;
        ++min_time;
    }
    
    int getTotalTime() {
        return total_time;
    }
    
    int getMinTime() {
        return min_time;
    }
};

/**
 * Your BusBooking object will be instantiated and called as such:
 * BusBooking* obj = new BusBooking(n);
 * obj->toggle(seat);
 * int param_2 = obj->getTotalTime();
 * int param_3 = obj->getMinTime();
 */
 