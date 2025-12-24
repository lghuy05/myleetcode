#include <bits/stdc++.h>
#include <cmath>

using namespace std;
class Solution {
public:
  int missingNumber(const vector<int> &arr) {
    // int expected_sum = 0;
    // for (int i = arr[0]; i <= arr.back(); i++) {
    //   expected_sum += i;
    // }
    // int actual_sum = 0;
    // for (int i : arr) {
    //   actual_sum += i;
    // }
    // return expected_sum - actual_sum;
    int left = 0;
    int right = arr.size() - 1;
    while (left <= right) {
      int mid = (right - left) / 2 + left;
      if (arr[0] + mid != arr[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    return arr[0] + left;
  }
};

int main() {
  Solution testcase;
  cout << testcase.missingNumber({1, 2, 3, 5}) << endl;
  return 0;
}
