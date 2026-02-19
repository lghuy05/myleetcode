#include <bits/stdc++.h>

class Solution {
public:
  int countBinarySubstrings(string s) {
    int prev = 0;
    int current = 1;
    int ans = 0;
    for (int i = 1; i < s.size(); i++) {
      if (s[i] == s[i - 1]) {
        current++;
      } else {
        ans += min(prev, current);
        prev = current;
        current = 1;
      }
    }
    ans += min(prev, current);
    return ans;
  }
};
