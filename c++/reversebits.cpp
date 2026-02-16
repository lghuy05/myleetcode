#include <bits/stdc++.h>
#include <cstdint>

using namespace std;

class Solution {
public:
  uint32_t reverseBits(int n) {
    uint32_t ans = 0;
    for (int i = 0; i < 32; i++) {
      ans *= 2;
      ans += n % 2;
      n /= 2;
    }
    return ans;
  }
};
