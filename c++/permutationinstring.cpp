#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  bool checkInclusion(string s1, string s2) {
    if (s2.size() < s1.size())
      return false;
    vector<int> freq(26, 0);
    vector<int> permutation(26, 0);
    int n = s1.size();
    int left = 0;
    for (int i = 0; i < s1.size(); i++) {
      freq[s1[i] - 'a']++;
    }
    // first window ini
    for (int i = 0; i < s1.size() - 1; i++) {
      permutation[s2[i] - 'a']++;
    }

    for (int right = s1.size() - 1; right < s2.size(); right++) {
      permutation[s2[right] - 'a']++;
      if (permutation == freq)
        return true;
      permutation[s2[left++] - 'a']--;
    }
    return false;
  }
};
