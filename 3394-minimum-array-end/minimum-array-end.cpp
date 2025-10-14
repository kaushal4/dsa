class Solution {
public:
    long long minEnd(int n, int x) {
        unordered_set<int> flip_pos;
        int pos = 0;
        int some_num = x;
        while(some_num){
            int cur_pos = 1 << pos;
            if((x & cur_pos) > 0){
                flip_pos.insert(pos);
                some_num -= cur_pos;
            } 
            pos += 1;
        }
        int target_pos = 0;
        long long answer_pos = 0;
        long long answer = x;
        int target_exp = n-1;
        while(target_exp){
            long long cur_bit = 0;
            if(target_exp & (1 << target_pos)) {
                cur_bit = 1;
                target_exp = target_exp - (1<<target_pos);
            }
            while(true) {
                if(flip_pos.contains(answer_pos)) {
                    answer_pos+=1;
                } else {
                    answer += (cur_bit<<answer_pos);
                    answer_pos+=1;
                    break;
                }
            }
            target_pos++;
        }
        return answer;
    }
};