#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;
class Solution {
public:
  bool containsNearbyDuplicate(vector<int> &nums, int k) {
    unordered_set<int> hash;
    for (int num : nums) {
      if (hash.count(num)) {
        return true;
      }
      hash.insert(num);
    }
    return false;
  }
};
