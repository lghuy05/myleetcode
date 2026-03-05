#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int findMaxLength(vector<int> &nums) {
    vector<int> prefix(nums.size() + 1, 0);
    int ans = 0;
    unordered_map<int, int> hash;
    hash[0] = 0;
    for (int i = 1; i < prefix.size(); i++) {
      if (nums[i - 1] == 1) {
        prefix[i] = prefix[i - 1] + 1;
      } else {
        prefix[i] = prefix[i - 1] - 1;
      }
      if (hash.count(prefix[i])) {
        ans = max(ans, i - hash[prefix[i]]);
      }
      if (!hash.count(prefix[i]))
        hash[prefix[i]] = i;
    }
    return ans;
  }
};
