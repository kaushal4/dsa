struct mc {
    int movie, shop, cost;
    bool operator==(const mc& other) const {
        return this->movie == other.movie && this->shop == other.shop;
    }
};

const auto comp = [](const mc& a, const mc& b){
    if(a.cost != b.cost){
        return a.cost < b.cost;
    }
    if(a.shop != b.shop){
        return a.shop < b.shop;
    }
    return a.movie < b.movie;
};

using pi = pair<int, int>;

const auto costHash = [](const pi& a){
    return (hash<int>()(a.first) ^ hash<int>()(a.second) << 1);
};

class MovieRentingSystem {
public:
    set<mc, decltype(comp)> rentSet;
    map<int, set<mc, decltype(comp)>> shopMap;
    unordered_map<pi, int, decltype(costHash)> costInfo;

    MovieRentingSystem(int n, vector<vector<int>>& entries) :
    rentSet(comp),
    shopMap(),
    costInfo(10, costHash)
    {
        for(const auto& entry: entries){
            int movie = entry[1];
            int shop = entry[0];
            int cost = entry[2];
            shopMap[movie].insert({movie, shop, cost});
            costInfo[{movie, shop}] = cost;
        }
        
    }
    
    vector<int> search(int movie) {
        if(!shopMap.contains(movie)) return vector<int>();
        auto &shopSet = shopMap[movie];
        vector<int> ans;
        for(const mc& item: shopSet){
            ans.push_back(item.shop);
            if(ans.size() == 5) break;
        }
        return ans;
    }
    
    void rent(int shop, int movie) {
        if(!shopMap.contains(movie)) return;
        auto &shopSet = shopMap[movie];
        auto item = shopSet.find({movie, shop, costInfo[{movie, shop}]});
        mc itemObj = *item;
        shopSet.erase(item);
        rentSet.insert(itemObj);
    }
    
    void drop(int shop, int movie) {
        if(!rentSet.contains({movie, shop, costInfo[{movie, shop}]})) return;
        auto item = rentSet.find({movie, shop, costInfo[{movie, shop}]});
        mc itemObj = *item;
        rentSet.erase(item);
        shopMap[itemObj.movie].insert(itemObj);
    }
    
    vector<vector<int>> report() {
        vector<vector<int>> ans;
        for(const mc& item: rentSet){
            ans.push_back({item.shop, item.movie});
            if(ans.size() == 5) break;
        }
        return ans;
    }
};

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
 * vector<int> param_1 = obj->search(movie);
 * obj->rent(shop,movie);
 * obj->drop(shop,movie);
 * vector<vector<int>> param_4 = obj->report();
 */