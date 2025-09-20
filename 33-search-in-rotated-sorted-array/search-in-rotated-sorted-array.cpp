class Solution {
public:
    int mid_point(vector<int>& nums){
        int n = nums.size();
        int low = 0, high = n-1;
        int anchor = nums[low];
        int sol = -1;
        while(low <= high) {
            //cout<<low<<" "<<high<<endl;
            int mid = low + (high - low)/2;
            if(nums[mid] >= anchor){
                sol = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return sol;
    }

    int find(vector<int>& nums, int target, int low, int high){
        while(low <= high){
            int mid = low + (high - low)/2;
            if(nums[mid] == target) return mid;
            if(target < nums[mid]){
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int midp = mid_point(nums);
        //cout<<midp<<" "<<endl;
        int low_find = find(nums, target, 0, midp);
        if(low_find != -1) return low_find;
        return find(nums, target, midp +1, n-1);
    }
};