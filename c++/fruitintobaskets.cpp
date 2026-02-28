#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int totalFruit(vector<int> &fruits) {
    // TC: O(n), SC: O(1)
    int last = -1, secondLast = -1;
    int lastCount = 0;
    int ans = 0;
    int current = 0;
    for (fruit : fruits) {
      if (fruit == last || fruit == secondLast) {
        current++;
      } else {
        current = lastCount + 1;
      }

      if (fruit = last) {
        lastCount++;
      } else {
        lastCount = 1;
        secondLast = last;
        last = fruit;
      }
      ans = max(ans, current);
    }
    return ans;
  }
};
