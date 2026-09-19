class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int dist = 0;
        if (xCenter < x1 || xCenter > x2) {
            int d1 = x1 - xCenter, d2 = x2 - xCenter;
            dist += min(d1 * d1, d2 * d2);
        }

        if (yCenter < y1 || yCenter > y2) {
            int d1 = y1 - yCenter, d2 = y2 - yCenter;
            dist += min(d1 * d1, d2 * d2);
        }

        return (dist <= radius * radius);
    }
};
