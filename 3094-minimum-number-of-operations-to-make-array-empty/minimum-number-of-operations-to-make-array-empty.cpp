class Solution {
public:
    int findMin(int target){
        int ans = INT_MAX;
        int i = 0;
        while(target - (3 * i) >= 0){
            int curNum = target - (3*i);
            if(curNum % 2 == 0){
                ans = min(ans, i + curNum / 2);
            }
            i++;
        }
        return ans == INT_MAX?-1:ans;
    }
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> count;
        int ans = 0;
        for(int num : nums){
            count[num]+= 1;
        }
        for(const auto[key, value] : count){
            int curCount = findMin(value);
            if(curCount == -1) return -1;
            ans += curCount;
        }
        return ans;
    }
};