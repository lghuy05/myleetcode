#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int pivotIndex(vector<int> &nums) {
    vector<int> prefix(nums.size() + 1, 0);
    int ans = -1;
    for (int i = 1; i < prefix.size(); i++) {
      prefix[i] = prefix[i - 1] + nums[i - 1];
    }
    int sum = prefix[prefix.size() - 1];
    for (int i = 0; i < nums.size(); i++) {
      if (sum - prefix[i + 1] == prefix[i]) {
        ans = i;
        break;
      }
    }
    return ans;
  }
};
