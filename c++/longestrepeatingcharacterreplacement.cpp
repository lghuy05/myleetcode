#include <stdio.h>

using namespace std;
class Solution {
public:
  int characterReplacement(string s, int k) {
    // TC: O(n)
    int ans = 0;
    vector<int> freq(26, 0);
    int left = 0;
    int check = 0;
    for (int right = 0; right < s.size(); right++) {
      freq[s[right] - 'A']++;
      check = max(check, freq[s[right] - 'A']);
      while ((right - left + 1) - check > k) {
        freq[s[left] - 'A']--;
        left++;
      }
      ans = max(ans, right - left + 1);
    }

    return ans;
  }
};
