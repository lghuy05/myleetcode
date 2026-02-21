#include <bits/stdc++.h>

class Solution {
public:
  int countBits(int x) {
    // TC: O(n)
    int cnt = 0;
    while (x) {
      x &= (x - 1);
      cnt++;
    }
    return cnt;
  }

  int isPrime(int x) {
    if (x < 2)
      return false;
    for (int i = 2; i * i <= x; i++) {
      if (x % i == 0)
        return false;
    }
    return true;
  }

  int countPrimeSetBits(int left, int right) {
    int ans = 0;
    for (int x = left; x <= right; x++) {
      int bits = countBits(x);
      if (isPrime(bits))
        ans++;
    }
    return ans;
  }
};
