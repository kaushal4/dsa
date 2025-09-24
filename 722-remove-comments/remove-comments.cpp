class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        bool end_comment = false;
        vector<string> ans;
        string cur_content = "";
        for(const string&line: source){
            int n = line.size();
            bool line_break = false;
            bool skip_next = false;
            for(int i = 0; i < n; i++){
                if(skip_next){
                    skip_next = false;
                    continue;
                }
                if(end_comment){
                    if (line[i] == '*' && i!=n-1 && line[i + 1] == '/') {
                        end_comment = false;
                        skip_next = true;
                    }
                } else {
                    if(line[i] == '/' && i!=n-1 && line[i+1] == '/'){
                        line_break = true;
                        break;
                    } else if(line[i] == '/' && i!=n-1 && line[i+1] == '*'){
                        end_comment = true;
                        skip_next = true;
                    } else {
                        cur_content += line[i];
                    }
                }
            }
            if(!end_comment && !cur_content.empty()){
                ans.push_back(cur_content);
                cur_content = "";
            }
        }
        return ans;
    }
};