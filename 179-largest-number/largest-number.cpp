class Solution {
public:
    string largestNumber(vector<int>& nums) {
        auto comp = [](int a, int b)
        {
            return (to_string(a) + to_string(b)) > (to_string(b) + to_string(a));
        };
        sort(nums.begin(), nums.end(), comp);
        string sol = "";
        for(const auto& num: nums){
            sol += to_string(num);
        }
        return sol[0] == '0' ? "0" : sol;
    }
};