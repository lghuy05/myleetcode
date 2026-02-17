#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int countBits(int n) {
    int count = 0;
    while (n) {
      count += n % 2;
      n /= 2;
    }
    return count;
  }

  vector<string> readBinaryWatch(int turnedOn) {
    vector<string> ans;

    for (int h = 0; h < 12; h++) {
      for (int m = 0; m < 60; m++) {
        if (countBits(h) + countBits(m) == turnedOn) {
          string minute = (m < 10 ? "0" : "") + m;
          ans.push_back(to_string(h) + ":" + min);
        }
      }
    }
    return ans;
  }
};
