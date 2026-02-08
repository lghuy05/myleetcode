#include <bits/stdc++.h>

class Solution {
public:
  void moveZeroes(vector<int> &nums) {
    int left = 0;
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == 0) {
        left++;
        continue;
      }
      nums[i - left] = nums[i];
    }
    for (int i = nums.size() - left; i < nums.size(); i++) {
      nums[i] = 0;
    }
  }
};
