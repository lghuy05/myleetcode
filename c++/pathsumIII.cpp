#include <bits/stdc++.h>
#include <filesystem>
#include <functional>
#include <unordered_map>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

using namespace std;
class Solution {
public:
  /*Optimal solution: TC: O(n)
   *prefix sum idea approach
   *keep track the current prefix sum into hashmap
   *on nexts recursion if [new current sum - targetSum] existed in hashmap ->
   * path exist -> ans++
   */
  int ans = 0;
  unordered_map<long long, int> prefix;
  long long cur = 0;
  void dfs(TreeNode *root, int target) {
    if (!root)
      return;
    cur += root->val;
    ans += prefix[cur - target];
    prefix[cur]++;
    dfs(root->left, target);
    dfs(root->right, target);
    prefix[cur]--;
    cur -= root->val;
  }
  int pathSum(TreeNode *root, int targetSum) {
    prefix[0] = 1;
    dfs(root, targetSum);
    return ans;
  }
};
