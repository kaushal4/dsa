struct resultPair {
    ListNode* newhead;
    ListNode* newtail;
    ListNode* nexthead;
    void print(){
        bool didprint = false;
        if(newhead != nullptr){
            cout<<newhead->val<<" ";
            didprint = true;
        }
        if(newtail != nullptr){
            cout<<newtail->val<<" ";
            didprint = true;
        }
        if(nexthead != nullptr){
            cout<<nexthead->val<<" ";
            didprint = true;
        }
        if(didprint) cout<<endl;
    }
};

class Solution {
public:

    resultPair reverse(ListNode* head, int k){
        ListNode anchor = ListNode();
        anchor.next = head;
        int counter = 1;
        while(head != nullptr && counter < k){
            counter += 1;
            head = head->next;
        }
        if(counter < k || head == nullptr){
            return {anchor.next, head, nullptr};
        }
        head = anchor.next;
        ListNode* prev = nullptr;
        counter = 1;

        while(counter <= k){
            counter += 1;
            ListNode* temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }
        return {prev, anchor.next, head};
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode anchor = ListNode(-1, head);
        ListNode* prev = &anchor;

        while(prev != nullptr && head != nullptr) {
            resultPair rp = reverse(head, k);
            prev->next = rp.newhead;
            prev = rp.newtail;
            head = rp.nexthead;
        }
        return anchor.next;
    }
};

/**
 * 1,2,3
 * k = 2
 * 
 */