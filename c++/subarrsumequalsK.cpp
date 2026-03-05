#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;
class Solution {
public:
  int subarraySum(vector<int> &nums, int k) {
    unordered_map<int, int> hash;
    hash[0] = 1;
    int prefix = 0;
    int ans = 0;
    for (int n : nums) {
      prefix += n;
      if (hash.count(prefix - k)) {
        ans += hash[prefix - k];
      }
      hash[prefix]++;
    }
    return ans;
  }
};
