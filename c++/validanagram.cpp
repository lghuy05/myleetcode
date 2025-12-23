
#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;
class Solution {
public:
  bool isAnagram(string s, string t) {}
  unordered_map<char, int> mp;
  for (char i : s) {
    mp[i]++;
  }
  unordered_map<char, int> mp2;
  for (char i : t) {
    mp2[i]++;
  }
  if (mp == mp2) {
    return true;
  } else {
    return false;
  }
};
