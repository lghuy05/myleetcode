class Solution {
public:
  int totalFruit(vector<int> &fruits) {
    unordered_map<int, int> window;
    int ans = 0;
    int left = 0;
    int cur = 0;
    for (int i = 0; i < fruits.size(); i++) {
      window[fruits[i]]++;
      cur++;
      while (window.size() > 2) {
        window[fruits[left++]]--;
        if (window[fruits[left - 1]] == 0) {
          window.erase(fruits[left - 1]);
        }
        cur--;
      }
      ans = max(ans, cur);
    }
    return ans;
  }
};
