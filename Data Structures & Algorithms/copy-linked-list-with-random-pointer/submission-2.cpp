/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    unordered_map<Node*, Node*> map;

    Node* copyRandomList(Node* head) {
        // If its head is null, return null
        // If we created this already, return the already made copy (memoised)
        if (head == nullptr) return nullptr;
        if (map.count(head)) return map[head];

        // Create the copy
        // Then store the mapping BEFORE we recurse, this is so we can revisit random
        Node* copy = new Node(head->val);
        map[head] = copy;

        // Explore down all paths down the normal path like a linked list
        // Then use the map we created, to route the copied nodes since they're already created
        copy->next = copyRandomList(head->next);
        copy->random = map[head->random];
        return copy;
    }
};
