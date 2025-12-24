#include <algorithm>
#include <bits/stdc++.h>
#include <vector>

using namespace std;
class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    vector<vector<string>> result = {};
    unordered_map<string, vector<string>> mp;
    for (string i : strs) {
      string old_i = i;
      sort(i.begin(), i.end());
      if (!mp.count(i)) {
        mp[i] = {old_i};
      } else {
        mp[i].push_back(old_i);
      }
    }
    for (const auto &[key, value] : mp) {
      result.push_back(value);
    }
    return result;
  }
};
