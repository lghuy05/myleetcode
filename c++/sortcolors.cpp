#include <bits/stdc++.h>

class Solution {
public:
  void sortColors(vector<int> &nums) {
    // int red = 0, white = 0, blue = 0;
    // for (int i = 0; i < nums.size(); i++) {
    //   if (nums[i] == 0)
    //     red++;
    //   else if (nums[i] == 1)
    //     white++;
    //   else if (nums[i] == 2)
    //     blue++;
    // }
    //
    // for (int i = 0; i < nums.size(); i++) {
    //   if (red > 0) {
    //     nums[i] = 0;
    //     red--;
    //   } else if (white > 0) {
    //     nums[i] = 1;
    //     white--;
    //
    //   } else if (blue > 0) {
    //     nums[i] = 2;
    //     blue--;
    //   }
    // }
    int low = 0, mid = 0, high = nums.size() - 1;
    while (mid <= high) {
      if (nums[mid] == 0) {
        swap(nums[mid++], nums[low++]);
      } else if (nums[mid] == 1) {
        mid++;
      } else {
        swap(nums[mid], nums[high--]);
      }
    }
  }
};
