#include <algorithm>
#include <bits/stdc++.h>
#include <cstdint>

class Solution {
public:
  int maxArea(vector<int> &height) {
    int left = 0, right = height.size() - 1;
    int max_vol = 0;
    while (left < right) {
      max_vol = std::max(max_vol, (right - left) *
                                      std::min(height[left], height[right]));

      if (height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    }
    return max_vol;
  };
};
