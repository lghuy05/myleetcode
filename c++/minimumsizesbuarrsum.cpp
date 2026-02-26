#include <bits/stdc++.h>
#include <cstdint>

using namespace std;
class Solution {
public:
  int minSubArrayLen(int target, vector<int> &nums) {
    // TC: O(n), SC: O(1)
    int ans = nums.size() + 1;
    int left = 0;
    int current = 0;
    int count = 0;
    for (int right = 0; right < nums.size(); right++) {
      current += nums[right];
      count++;
      while (current >= target) {
        ans = min(ans, count);
        current -= nums[left++];
        count--;
      }
    }
    return (ans == nums.size() + 1) ? 0 : ans;
  }
};
