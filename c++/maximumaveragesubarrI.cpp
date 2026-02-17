#include <bits/stdc++.h>

class Solution {
public:
  double findMaxAverage(vector<int> &nums, int k) {
    int left = 0, right = k - 1;
    int sum = 0;
    double ans = -1e9;
    for (int i = left; i <= right; i++) {
      sum += nums[i];
    }
    double current = (double)sum / k;
    ans = current;
    right++;
    while (right < nums.size()) {
      current -= nums[left] / k;
      left++;
      current += nums[right] / k;
      right++;
      ans = max(ans, current);
    }
    return ans;
  }
};
