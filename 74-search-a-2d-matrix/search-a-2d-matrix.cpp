class Solution {
public:
    int binarySearchRow(vector<vector<int>>& matrix, int target){
        int low = 0;
        int high = matrix.size() - 1;
        int sol = -1;

        while(low <= high){
            int mid = low + (high - low)/2;
            int cur = matrix[mid][0];
            if(cur <= target) {
                sol = mid;
                low += 1;
            } else{
                high -= 1;
            }
        }
        return sol;
    }

    int binarySearchColumn(vector<vector<int>>& matrix,int row, int target){
        int low = 0;
        int high = matrix[row].size() - 1;

        while(low <= high){
            int mid = low + (high - low)/2;
            int cur = matrix[row][mid];
            if(cur == target) {
                return true;
            } else if(cur < target) {
                low += 1;
            } else{
                high -= 1;
            }
        }
        return false;
    }

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = binarySearchRow(matrix, target);
        if(row == -1) return false;
        return binarySearchColumn(matrix, row, target);
    }
};