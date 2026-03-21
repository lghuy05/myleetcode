class Solution {
public:
  int longestConsecutive(vector<int> &nums) {
    int res = 0;
    unordered_set<int> hash;
    for (int num : nums) {
      hash.insert(num);
    }
    for (int num : nums) {
      int current;
      int streak;
      if (!hash.count(num - 1)) {
        current = num;
        streak = 1;
        while (hash.count(current + 1)) {
          streak += 1;
          current += 1;
        }
        res = max(streak, res);
      }
    }
    return res;
  }
};
