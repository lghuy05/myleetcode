#include <bits/stdc++.h>
#include <iterator>

using namespace std;

class Solution {
public:
  long long maximumHappinessSum(vector<int> &happiness, int k) {
    sort(happiness.begin(), happiness.end());
    int result = 0;
    int i = 0;
    while (k) {
      long long popval = happiness.back();
      happiness.pop_back();
      if (popval - i > 0) {
        result += popval - i;
      }
      k -= 1;
      i += 1;
    }
    return result;
  }
};
