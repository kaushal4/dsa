class Solution {
public:
    int minSol(int num) {
        if (num == 2){
            return -1;
        }
        short pos = 0;
        int secondary = 0; 
        while(num > 0) {
            if((num & (1 << pos)) == (1 << pos)) {
                secondary = secondary + (1 << pos);
                num = num - (1 << pos);
                pos += 1;
            } else {
                break;
            }
        }
        pos -= 1;
        secondary = secondary - (1 << pos);
        num = num + secondary;
        return num;
    }
    vector<int> minBitwiseArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, INT_MAX);
        for(int i = 0; i < n; i++){
            ans[i] = minSol(nums[i]);
        }
        return ans;
    }
};