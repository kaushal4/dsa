struct dll {
    dll* prev;
    dll* next;
    int key;
    int value;
};

class LRUCache {
public:
    int capacity; 
    dll* head;
    dll* tail;
    int occupancy;
    unordered_map<int, dll*> lru_map;

    LRUCache(int capacity) {
        this->capacity = capacity;
        occupancy = 0;
        head = nullptr;
        tail = nullptr;
        lru_map = unordered_map<int, dll*>();
    }

    void pushLeft(int key, int value){
        dll* node = new dll(nullptr, nullptr, key, value);
        pushLeft(node);
    }

    void pushLeft(dll* node){
        lru_map[node->key] = node;
        if(head != nullptr) {
            node->next = head;
            head->prev = node;
            head = node;
        } else{
            head = node;
            tail = node;
        }
        occupancy += 1;
    }

    dll* popRight() {
        dll* node = tail;

        if (node == nullptr) return nullptr;
        lru_map.erase(node->key);
        occupancy -= 1;

        dll* prev = node->prev;
        if(prev == nullptr){
            head = nullptr;
            tail = nullptr;
        } else {
            prev->next = nullptr;
            tail = prev;
        }
        return node;
    }

    dll* popNode(dll* node){
        if(node == nullptr || !lru_map.contains(node->key)) return nullptr;

        if(node == tail){
            return popRight();
        } 
        lru_map.erase(node->key);
        occupancy -= 1;
        if(node == head) {
            dll* next = node->next;
            next->prev = nullptr;
            head = next;
            return node;
        }
        dll* prev = node->prev;
        dll* next = node->next;
        prev->next = next;
        next->prev = prev;
        return node;
    }

    void promote(dll* node){
        popNode(node);
        pushLeft(node);
    }
    
    int get(int key) {
        if(lru_map.contains(key)){
            promote(lru_map[key]);
            return lru_map[key]->value;
        }
        return -1;
    }

    void put(int key, int value) {
        if(lru_map.contains(key)){
            lru_map[key]->value = value;
            promote(lru_map[key]);
            return;
        }
        if(occupancy == capacity){
            dll* poped_node = popRight();
            delete(poped_node);
            pushLeft(key, value);
            return;
        }
        pushLeft(key, value);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */