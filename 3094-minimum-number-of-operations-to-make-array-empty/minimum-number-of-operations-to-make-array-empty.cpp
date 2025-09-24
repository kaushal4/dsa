class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }

        int total_ops = 0;
        for (auto const& [num, count] : counts) {
            // It's impossible to clear a single element
            if (count == 1) {
                return -1;
            }
            
            // Use the O(1) mathematical formula
            total_ops += (count + 2) / 3;
        }
        
        return total_ops;
    }
};