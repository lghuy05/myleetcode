#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  bool check(int n) {
    return (n >= 'a' && n <= 'z') || (n >= 'A' && n <= 'Z') ||
           (n >= '0' && n <= '9');
  }

  bool isPalindrome(string s) {

    int left = 0;
    int right = s.size() - 1;

    while (left < right) {

      while (left < right && !check(s[left]))
        left++;
      while (left < right && !check(s[right]))
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
