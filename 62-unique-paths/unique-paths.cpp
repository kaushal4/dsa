class Solution {
public:
    int uniquePaths(int m, int n) {
        // We need (m-1) down moves and (n-1) right moves
        // Total moves = (m-1) + (n-1) = m + n - 2
        // Answer = C(m+n-2, m-1) = C(m+n-2, n-1)
        
        int totalMoves = m + n - 2;
        int downMoves = m - 1;
        int rightMoves = n - 1;
        
        // Choose the smaller of the two to minimize computation
        int r = min(downMoves, rightMoves);
        
        // Calculate C(totalMoves, r) = totalMoves! / (r! * (totalMoves-r)!)
        // We'll compute this iteratively to avoid overflow
        long long result = 1;
        
        for (int i = 0; i < r; i++) {
            result = result * (totalMoves - i) / (i + 1);
        }
        
        return (int)result;
    }
};