#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int findLengthOfLCIS(vector<int> &nums) {
    // TC: O(n),SC: O(1)
    int ans = 1;
    int left = 1;
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] > nums[i - 1]) {
        left++;
        ans = max(left, ans);
      } else {
        left = 1;
      }
    }
    return ans;
  }
};

int main() {
  Solution sol;
  vector<int> nums = {1, 3, 5, 4, 7};
  cout << sol.findLengthOfLCIS(nums) << endl;
}
