class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
         int achor = nums[0];
         int low = 1, high = n-1;
         while(low <= high) {
            int mid = low + (high - low)/2;
            if(nums[mid] < nums[mid-1]) {
                return nums[mid];
            } else if(nums[mid] > achor){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
         }
         return achor;
    }
};