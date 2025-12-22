#include <bits/stdc++.h>

class Solution {
public:
  int mirrorDistance(int n) {
    int N = n;
    int m = 0;
    while (N) {
      m *= 10;
      m += N % 10;
      N /= 10;
    }
    return abs(m - n);
  }
};

int main() {
  Solution testcase;
  std::cout << testcase.mirrorDistance(25);
}
