#include <bits/stdc++.h>
#include <vector>

using namespace std;
class Solution {
public:
  int largestAltitude(vector<int> &gain) {
    vector<int> prefix(gain.size() + 1, 0);
    int ans = 0;
    for (int i = 1; i < prefix.size(); i++) {
      prefix[i] = prefix[i - 1] + gain[i - 1];
      ans = max(ans, prefix[i]);
    }
    return ans;
  }
};
