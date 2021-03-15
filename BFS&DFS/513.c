struct TreeNode {
     int val;
     struct TreeNode *left;
     struct TreeNode *right;
};
#define inf 0x3f3f3f

int findBottomLeftValue(struct TreeNode* root){
    struct TreeNode* queue[inf];
    queue[0] = root;
    int head = 0;
    int rear = 0;
    int ans = 0;
    while (rear >= head) {
        int num = rear - head;
        ans = queue[head]->val;
        for (int i = 0; i <= num; i++) {
            struct TreeNode* temp = queue[head];
            head++;
            if (temp->left) {
                queue[++rear] = temp->left;
            }
            if (temp->right) {
                queue[++rear] = temp->right;
            }
        }
    }
    return ans;
}