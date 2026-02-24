#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int ans = 0;
    int left = 0;
    vector<int> memo(128, 0);

    for (int right = 0; right < s.size(); right++) {
      memo[s[right] - ' ']++;
      if (memo[s[right] - ' '] > 1) {
        while (memo[s[right] - ' '] > 1) {
          memo[s[left] - ' ']--;
          left++;
        }
      }
      ans = max(ans, right - left + 1);
    }
    return ans;
  }
};
