#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;
class Solution {
public:
  int subarraysDivByK(vector<int> &nums, int k) {
    int ans = 0;
    unordered_map<int, int> freq;
    int prefix = 0;
    freq[0] = 1;
    for (int n : nums) {
      prefix += n;
      int mod = ((prefix % k) + k) % k;
      ans += freq[mod];
      freq[mod]++;
    }
    return ans;
  }
};

//[0, 4, 9, 9, 7, 4, 5]
// arr[i:j] = prefix[j] - prefix[i-1]
// prefix[j] - prefix[i-1]% k == 0
