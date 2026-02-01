class Solution {
public:
  char nextGreatestLetter(vector<char> &letters, char target) {
    int i = 0;
    int n = letters.size();
    while (i < n && letters[i] <= target) {
      i += 1;
    }
    if (i == n) {
      return letters[0];
    }
    return letters[i];
  }
};
