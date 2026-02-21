#include <bits/stdc++.h>

class Solution {
public:
  int minimumRecolors(string blocks, int k) {
    /*pattern: sliding window
     *min replacement = min of the letter in a window
     *
     *TC: O(n), SP: (O1)
     */
    int whites = 0;
    for (int i = 0; i < k; i++) {
      if (blocks[i] == 'W')
        whites++;
    }
    int ans = whites;
    for (int i = k; i < blocks.size(); i++) {
      if (blocks[i - k] == 'W')
        whites--;
      if (blocks[i] == 'W')
        whites++;
      ans = min(ans, whites);
    }
    return ans;
  }
};
