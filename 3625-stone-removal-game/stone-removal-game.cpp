class Solution {
public:
    bool canAliceWin(int n) {
        int agg = 0;
        for(int i=10;i>=0;i--) {
            agg += i;
            if (n < agg) {
                if (i%2 == 0) return false;
                else return true;
            }
        }
        return false;
    }
};