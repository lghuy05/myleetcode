#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;
class Solution {
public:
  // sliding window, expect TC: O(n), SP: O(1)
  int count(vector<int> &nums, int goal) {
    int ans = 0;
    int sum = 0;
    int left = 0;
    for (int right = 0; right < nums.size(); right++) {
      sum += nums[right];
      if (sum > goal) {
        sum -= nums[left++];
      }
      ans += right - left + 1;
    }
    return ans;
  }

  int numSubarraysWithSum(vector<int> &nums, int goal) {

    // Time complexity: O(n), space complexity: O(1)
    // prefix sum

    // int ans = 0;
    // unordered_map<int, int> freq;
    // int prefix = 0;
    // freq[0] = 1;
    // for (int num : nums) {
    //   prefix += num;
    //   ans += freq[prefix - goal];
    //   freq[prefix]++;
    // }
    // return ans;
    //
    // sliding window

    return count(nums, goal) - count(nums, goal - 1);
  }
};
