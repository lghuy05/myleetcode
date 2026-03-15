#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hash;
    int remain;
    for (int i = 0; i < nums.size(); i++) {
      remain = target - nums[i];
      if (hash.count(remain)) {
        return {hash[remain], i};
      }
      hash[nums[i]] = i;
    }
    return {0};
  }
};
