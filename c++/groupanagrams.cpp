using namespace std;
class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    unordered_map<string, vector<string>> hash;
    vector<vector<string>> ans;
    for (string num : strs) {
      string key = num;
      sort(key.begin(), key.end());
      hash[key].push_back(num);
    }
    for (auto &pair : hash) {
      ans.push_back(pair.second);
    }
    return ans;
  }
};
