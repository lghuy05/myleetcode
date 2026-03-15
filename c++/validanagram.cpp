
#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;
class Solution {
public:
  bool isAnagram(string s, string t) {
    unordered_map<int, int> freq1;
    unordered_map<int, int> freq2;
    for (char num : s) {
      freq1[num]++;
    }
    for (char num : t) {
      freq2[num]++;
    }
    return freq1 == freq2;
  }
};
