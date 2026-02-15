#include <algorithm>
#include <bits/stdc++.h>

class Solution {
public:
  string addBinary(string a, string b) {
    /* a pointer tracking where to add?
     *two pointer on a and b then go from end to start
     *
     *the idea is how we adding binary irl
     *add a and b, add mod of (a+b) to result
     *carry store (a+b)/2 and be set to next sum (basically mean add carry at
     * next iteration)
     */
    int pa = a.size() - 1;
    int pb = b.sisze() - 1;
    int carry = 0;
    string ans = "";
    while (pa >= 0 || pb >= 0 || carry) {
      int sum = carry;

      if (pa >= 0)
        sum += a[pa--] - '0';
      if (pb >= 0)
        sum += b[pb--] - '0';

      ans += (sum % 2) + '0';
      carry = sum / 2;
    }
    std::reverse(ans.begin(), ans.end());
    return ans;
  }
};
