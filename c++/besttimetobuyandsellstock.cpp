#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int maxProfit(vector<int> &prices) {
    int left = 0;
    int right = 1;
    int n = prices.size();
    int result = 0;
    while (right < n) {
      if (prices[right] > prices[left]) {
        int res = prices[right] - prices[left];
        if (res > result) {
          result = res;
        }
      } else {
        left = right;
      }
      right += 1;
    }
    return result;
  }
};
