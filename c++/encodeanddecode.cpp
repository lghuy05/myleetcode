class Solution {
public:
  string encode(vector<string> &strs) {
    string encoded = "";
    for (string character : strs) {
      encoded += character;
      encoded += '`';
    }
    return encoded;
  }

  vector<string> decode(string s) {
    vector<string> decoded;
    string word = "";
    for (char character : s) {
      if (character == '`') {
        decoded.push_back(word);
        word = "";
      } else {
        word += character;
      }
    }
    return decoded;
  }
};
