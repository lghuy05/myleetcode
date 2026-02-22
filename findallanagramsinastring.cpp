#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  vector<int> findAnagrams(string s, string p) {
    vector<int> ans;

    if (p.size() > s.size())
      return ans;

    vector<int> p_cnt(26, 0), s_cnt(26, 0);
    for (char c : p) {
      p_cnt[c - 'a']++;
    }

    int matches = 0;
    for (int i = 0; i < p.size(); i++) {
      s_cnt[s[i] - 'a']++;
    }
    for (int i = 0; i < 26; i++) {
      if (p_cnt[i] == s_cnt[i])
        matches++;
    }

    int left = 0;
    for (int right = p.size(); right < s.size(); right++) {
      if (matches == 26)
        ans.push_back(left);
      int r = s[right] - 'a';
      int l = s[left] - 'a';

      s_cnt[r]++;
      if (s_cnt[r] == p_cnt[r])
        matches++;
      else if (s_cnt[r] == p_cnt[r] + 1)
        matches--;

      s_cnt[l]--;
      if (s_cnt[l] == p_cnt[l])
        matches++;
      else if (s_cnt[l] == p_cnt[l] - 1)
        matches--;
      left++;
    }
    if (matches == 26)
      ans.push_back(left);
    return ans;
  }
};
