/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int min_dist = INT_MAX, first_idx = 0, prev_idx = 0, curr_idx = 1;
        ListNode* prev = head;
        ListNode* curr = head->next;
        while (curr->next) {
            if ((curr->val < prev->val and curr->val < curr->next->val) or (curr->val > prev->val and curr->val > curr->next->val)) {
                if (prev_idx == 0)
                    first_idx = curr_idx;
                else
                    min_dist = min(min_dist, curr_idx - prev_idx);
                
                prev_idx = curr_idx;
            }
                
            ++curr_idx;
            prev = curr;
            curr = curr->next;
        }
        
        vector<int> result(2, -1);
        if (min_dist == INT_MAX)
            return result;

        result[0] = min_dist;
        result[1] = prev_idx - first_idx;
        return result;
    }
};
