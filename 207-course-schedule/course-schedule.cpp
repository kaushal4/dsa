class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        for(auto& prereq : prerequisites) {
            int course = prereq[0];
            int dependency = prereq[1];
            graph[dependency].push_back(course);
        }

        unordered_set<int> active;
        unordered_set<int> done;
        bool sol = true;

        for(int i = 0; i < numCourses; i++){
            if(!done.contains(i)){
                sol = sol && dfs(graph, active, done, i);
            }
        }
        return sol;
    }

    bool dfs(vector<vector<int>>& prerequisites, unordered_set<int>& active, unordered_set<int>& done, int node) {
        if(done.contains(node)) return true;
        if(active.contains(node)) return false;
        active.insert(node);
        bool sol = true;
        for(const int preq: prerequisites[node]){
            sol = sol && dfs(prerequisites, active, done, preq);
        }
        done.insert(node);
        active.erase(node);
        return sol;
    }
};