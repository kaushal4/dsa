class Solution {
public:
    string getSmallestString(string s, int k) {
        int budget = k;
        int n = s.size();
        string t = "";
        for(int i = 0; i < n; i++){
            int max_cost = min(s[i] - 97, 123 - s[i]);
            if(max_cost <= budget){
                t += 'a';
                budget -= max_cost;
            } else {
                t += s[i] - budget;
                budget = 0;
            }
        }
        return t;
    }
};