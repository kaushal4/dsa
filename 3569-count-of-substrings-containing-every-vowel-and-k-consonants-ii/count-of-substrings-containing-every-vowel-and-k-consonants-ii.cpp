class Solution {
public:
    long long countOfSubstrings(string word, int k) {
        return atLeastK(word, k) - atLeastK(word, k + 1);
    }
    
private:
    long long atLeastK(string& word, int k) {
        int n = word.size();
        unordered_set<char> vowelSet = {'a','e','i','o','u'};
        unordered_map<char, int> vowelCount;
        int consonants = 0;
        long long result = 0;
        int left = 0;
        
        for (int right = 0; right < n; right++) {
            // Add character at right
            if (vowelSet.count(word[right])) {
                vowelCount[word[right]]++;
            } else {
                consonants++;
            }
            
            // Shrink window while valid (>= k consonants and all 5 vowels)
            while (consonants >= k && vowelCount.size() == 5) {
                result += n - right;  // All substrings [left..right], [left..right+1], ..., [left..n-1]
                
                // Remove left character
                if (vowelSet.count(word[left])) {
                    vowelCount[word[left]]--;
                    if (vowelCount[word[left]] == 0) {
                        vowelCount.erase(word[left]);
                    }
                } else {
                    consonants--;
                }
                left++;
            }
        }
        
        return result;
    }
};