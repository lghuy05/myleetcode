class Solution {
public:
  vector<int> twoSum(vector<int> &numbers, int target) {
    int left = 0;
    int right = numbers.size() - 1;
    int remain;
    while (left < right) {
      remain = target - numbers[right];
      if (remain == numbers[left]) {
        return {left + 1, right + 1};
      } else if (remain < numbers[left]) {
        right--;
      } else {
        left++;
      }
    }
    return {left + 1, right + 1};
  }
};
