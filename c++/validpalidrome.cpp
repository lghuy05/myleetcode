#include <bits/stdc++.h>

class Solution {
public:
  bool isPalindrome(string s) {
    int left = 0;
    int right = s.size() - 1;

    while (left < right) {
      while (left < right && !((s[left] >= 'A' && s[left] <= 'Z') ||
                               (s[left] >= 'a' && s[left] <= 'z')))
        left++;

      while (left < right && !((s[right] >= 'A' && s[right] <= 'Z') ||
                               (s[right] >= 'a' && s[right] <= 'z')))
        right--;

      if (s[left] >= 'A' && s[left] <= 'Z')
        s[left] += ('a' - 'A');
      if (s[right] >= 'A' && s[right] <= 'Z')
        s[right] += ('a' - 'A');

      if (s[left] != s[right])
        return false;

      left++;
      right--;
    }
    return true;
  }
};
