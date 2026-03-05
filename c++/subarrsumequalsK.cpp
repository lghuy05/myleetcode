#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int subarraySum(vector<int> &nums, int k) {
    vector<int> prefix(nums.size() + 1, 0);
    for (int i = 1; i < prefix.size(); i++) {
      prefix[i] = prefix[i - 1] + nums[i - 1];
    }
    int ans = 0;
    for (int j = 2; j < prefix.size(); j++) {
      for (int i = 1; i < j; i++) {
        if (prefix[j] - prefix[i] == k) {
          ans++;
        }
      }
    }
    return ans;
  }
};
