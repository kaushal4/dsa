struct timedValues {
    int timestamp;
    string value;
};

class TimeMap {
public:
    map<string, vector<timedValues>> timedMap;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        if(!timedMap.contains(key)){
            timedMap[key] = vector<timedValues>();
        }
        timedMap[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        if(!timedMap.contains(key)){
            return  "";
        }
        vector<timedValues>& timed_vector = timedMap[key];
        int n = timed_vector.size();
        int low = 0, high = n-1;
        string sol = "";
        while(low <= high){
            int mid = low + (high - low)/2;
            if(timed_vector[mid].timestamp <= timestamp){
                sol = timed_vector[mid].value;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return sol;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */