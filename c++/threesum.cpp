class Solution {
public:
  vector<vector<int>> threeSum(vector<int> &nums) {
    int n = nums.size();
    vector<vector<int>> res;
    sort(nums.begin(), nums.end());
    for (int i = 0; i < n - 2; i++) {
      int left = i + 1;
      int right = n - 1;
      if (i > 0 && nums[i] == nums[i - 1])
        continue;
      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];
        if (sum < 0) {
          left++;
        } else if (sum > 0) {
          right--;
        } else if (sum == 0) {
          res.push_back({nums[i], nums[left], nums[right]});
          while (left < right && nums[left + 1] == nums[left])
            left++;
          while (left < right && nums[right - 1] == nums[right])
            right--;
          left++;
          right--;
        }
      }
    }
    return res;
  }
};
