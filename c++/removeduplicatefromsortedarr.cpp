#include <bits/stdc++.h>

class Solution {
public:
  int removeDuplicates(vector<int> &nums) {
    // two pointer
    int track = nums[0];
    int prev = 1;
    int ans = 1;
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] != track) {
        track = nums[i];
        nums[prev] = nums[i];
        prev++;
        ans++;
      }
    }
    return ans;
  }
};
