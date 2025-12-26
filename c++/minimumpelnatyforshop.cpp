#include <algorithm>
#include <climits>
#include <string>
#include <vector>

class Solution {
public:
  int bestClosingTime(std::string customers) {
    int n = customers.size();
    std::vector<int> prefix(n + 2, 0);
    std::vector<int> postfix(n + 2, 0);

    for (int i = 0; i < n; i++) {
      if (customers[i] == 'N') {
        prefix[i + 2] = prefix[i + 1] + 1;
      } else {
        prefix[i + 2] = prefix[i + 1];
      }
    }

    for (int i = n - 1; i >= 0; i--) {
      if (customers[i] == 'Y') {
        postfix[i + 1] = postfix[i + 2] + 1;
      } else {
        postfix[i + 1] = postfix[i + 2];
      }
    }

    int min_penalty = INT_MAX;
    int result = 0;
    int day = 0;

    for (int i = 1; i <= n + 1; i++) {
      int penalty = prefix[i] + postfix[i];
      if (min_penalty > penalty) {
        min_penalty = penalty;
        result = day;
      }
      day++;
    }

    return result;
  }
};
