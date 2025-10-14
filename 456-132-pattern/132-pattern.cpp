class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return false;
        
        stack<int> st;
        int third = INT_MIN;  // The "2" in 132 pattern (nums[k])
        
        // Traverse from right to left
        for (int i = n - 1; i >= 0; i--) {
            // If current element < third, we found the "1"!
            if (nums[i] < third) return true;
            
            // Pop elements smaller than current from stack
            // These become candidates for "2" (nums[k])
            while (!st.empty() && nums[i] > st.top()) {
                third = st.top();  // Update the best "2" we've found
                st.pop();
            }
            
            // Current element is a candidate for "3" (nums[j])
            st.push(nums[i]);
        }
        
        return false;
    }
};