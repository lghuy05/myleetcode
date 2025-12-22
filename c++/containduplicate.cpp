#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  bool hasDuplicate(vector<int> &nums) {
    unordered_set<int> existed;
    for (int i : nums) {
      if (!existed.count(i)) {
        existed.insert(i);
      } else {
        return true;
      }
    }
    return false;
  }
};
