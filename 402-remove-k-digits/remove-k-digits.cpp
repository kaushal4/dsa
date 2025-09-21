class Solution {
public:
    string removeKdigits(string num, int k) {
        string result;
        int n = num.size();
        int budget = k;
        for(int i = 0; i < n; i++) {
            char cur_num = num[i];
            while(!result.empty() && budget > 0){
                if(result.back() > cur_num){
                    result.pop_back();
                    budget -= 1;
                } else break;
            }
            if(!result.empty() || cur_num != '0'){
                result.push_back(cur_num);
            }
        }
        while (!result.empty() && budget > 0) {result.pop_back(); budget -= 1;}
        return result == "" ? "0" : result;
    }
};