class Solution {
public:
    void printVec(vector<int>& pos){
        for(int i = 0; i < pos.size(); i++){
            cout<<pos[i]<<" ";
        }
        cout<<endl;
    }

    bool bs(vector<int>& pos, int minJump, int maxJump, int achor, int max_size){
        int n = pos.size();
        int low = 0;
        int high = n-1;
        while(low <= high){
            int mid = low + (high - low)/2;
            int cur_pos = pos[mid];
            if(cur_pos + minJump <= achor && achor <= min(cur_pos + maxJump, max_size)){
                return true;
            } else if (cur_pos + minJump > achor) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return false;
    }

    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();
        vector<int> pos{0};
        for(int i = 1; i < n; i++){
            if(s[i] == '0' && bs(pos, minJump, maxJump, i, n-1)){
                pos.push_back(i);
            }
        }
        if(pos.back() == n-1)return true;
        return false;
    }
};