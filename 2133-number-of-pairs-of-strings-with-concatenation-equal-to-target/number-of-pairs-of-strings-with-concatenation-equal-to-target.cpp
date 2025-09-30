class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
        unordered_map<string, unordered_set<int>> numsMap;
        int ans = 0;
        for(int i = 0; i < nums.size(); i++){
            numsMap[nums[i]].insert(i);
        }
        for(int cur = 0; cur < nums.size(); cur++){
            string num = nums[cur];
            int i = 0;
            while(i < num.size() && i < target.size()){
                if(num[i] == target[i]){
                    i++;
                }else {
                    break;
                }
            }
            if(i == num.size() && i < target.size()){
                string secondPart = target.substr(i);
                if(numsMap.contains(secondPart)){
                    auto pos = numsMap[secondPart];
                    int count = pos.size();
                    if(pos.contains(cur)) count --;
                    ans += count;
                }
            }
        }
        return ans;
    }
};