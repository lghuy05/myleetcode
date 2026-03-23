class Solution {
public:
  int maxArea(vector<int> &heights) {
    // idea container depend on max(min(left, right)*(right - left))
    int left = 0;
    int right = heights.size() - 1;
    int res = 0;
    while (left < right) {
      int height = min(heights[left], heights[right]);
      int base = right - left;
      res = max(res, base * height);
      if (heights[left] <= heights[right]) {
        left++;
      } else {
        right--;
      }
    }
    return res;
  }
};
