#include <bits/stdc++.h>

class Solution {
public:
  int trap(vector<int> &height) {
    int left = 0;
    int right = height.size() - 1;
    int ans = 0;
    int maxLeft = height[left];
    int maxRight = height[right];
    while (left < right) {
      if (maxLeft <= maxRight) {
        if (maxLeft - height[++left] > 0) {
          ans += maxLeft - height[left];
        } else {
          maxLeft = height[left];
        }

      } else {
        if (maxRight - height[--right] > 0) {
          ans += maxRight - height[right];
        } else {
          maxRight = height[right];
        }
      }
    }
    return ans;
  }
};
