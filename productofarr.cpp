class Solution {
public:
  vector<int> productExceptSelf(vector<int> &nums) {
    int n = nums.size();
    vector<int> prefix(n, 1);
    prefix[0] = nums[0];
    vector<int> postfix(n, 1);
    postfix[n - 1] = nums[n - 1];
    for (int i = 1; i < n; i++) {
      prefix[i] = prefix[i - 1] * nums[i];
    }
    for (int i = n - 2; i >= 0; i--) {
      postfix[i] = postfix[i + 1] * nums[i];
    }
    vector<int> result(n, 1);
    for (int i = 0; i < n; i++) {
      int left = (i > 0) ? prefix[i - 1] : 1;
      int right = (i < n - 1) ? postfix[i + 1] : 1;
      result[i] = left * right;
    }
    return result;
  }
};
