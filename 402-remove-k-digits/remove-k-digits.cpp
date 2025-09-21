class Solution {
public:
    string removeKdigits(string num, int k) {
        int n = num.length();
        
        // If we can remove all digits, the result is "0"
        if (k >= n) {
            return "0";
        }
        
        // The length of the final, smallest number
        int result_len = n - k;
        
        // If the result would be empty, it's "0"
        if (result_len == 0) {
            return "0";
        }

        string result = "";
        
        // A min-heap storing {digit, original_index}
        // The `greater` comparator makes it a min-heap on the first element of the pair.
        priority_queue<pair<char, int>, vector<pair<char, int>>, greater<pair<char, int>>> pq;
        
        int last_picked_index = -1; // Index of the last digit added to our result
        int scan_ptr = 0;           // Pointer to scan through the input `num`

        // We loop `result_len` times to build our final number
        for (int i = 0; i < result_len; ++i) {
            // 1. EXPAND THE WINDOW
            // The window of candidates for the i-th digit of the result
            // extends up to index k+i in the original string. We add all
            // numbers in this new range to our heap.
            int window_end = k + i;
            for (; scan_ptr <= window_end; ++scan_ptr) {
                pq.push({num[scan_ptr], scan_ptr});
            }
            
            // 2. FIND A VALID MINIMUM
            // The smallest digit might be at an index before the last digit we picked,
            // which is invalid. We pop from the heap until we find a digit whose
            // original index is valid (i.e., comes after the last one we picked).
            while (!pq.empty() && pq.top().second <= last_picked_index) {
                pq.pop();
            }
            
            // 3. SELECT THE BEST DIGIT
            // The top of the heap is now our best choice.
            if (!pq.empty()) {
                pair<char, int> best_choice = pq.top();
                pq.pop();
                
                // Append to result, but handle leading zeros.
                // A '0' is only added if the result string is not empty.
                if (result.length() > 0 || best_choice.first != '0') {
                    result += best_choice.first;
                }
                
                // Update the index of the last digit we picked.
                last_picked_index = best_choice.second;
            }
        }
        
        // If the result is empty, it means all chosen digits were leading zeros.
        if (result.empty()) {
            return "0";
        }
        
        return result;
    }
};