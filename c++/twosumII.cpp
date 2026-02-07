#include <bits/stdc++.h>

class Solution {
public:
  vector<int> twoSum(vector<int> &numbers, int target) {
    // two pointers #1
    // int left = 0;
    // int right = numbers.size() - 1;
    // while (left < right) {
    //   if (numbers[left] + numbers[right] > target) {
    //     right -= 1;
    //   } else if (numbers[left] + numbers[right] < target) {
    //     left += 1;
    //   } else {
    //     return {left + 1, right + 1};
    //   }
    // }
    // return {left + 1, right + 1};

    // hashmap
    unordered_map<int, int> mp;
    for (int i = 0; i < numbers.size(); i++) {
      int aim = target - numbers[i];
      if (mp.count(aim)) {
        return {mp[aim] + 1, i + 1};
      } else {
        mp[numbers[i]] = i;
      }
    }
    return {-1, -1};
  }
};
