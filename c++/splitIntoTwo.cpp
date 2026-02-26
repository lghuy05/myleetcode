#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
  int splitIntoTwo(vector<int> &arr) {
    /* Brute force
     for n elements, will have at most n-1 way to split
     choose index to split and slice into left and right portion
     calculate sum and see if for that slice sum(left) > sum(right)
     ans++
     expect TC: O(N*N)
    */

    /* Optimal prefix sum
    calculate prefix sum and postfix sum both forward and backward
    for each slice see if prefixsum(slice) > postfixsum(slice)
    ans++
    expect TC: O(N), SC: O(N)
    */

    int ans = 0;
    vector<int> prefix(arr.size() + 1, 0);
    vector<int> postfix(arr.size() + 1, 0);
    for (int i = 1; i < prefix.size(); i++) {
      prefix[i] = prefix[i - 1] + arr[i - 1];
    }
    for (int i = arr.size() - 1; i > -1; i--) {
      postfix[i] = postfix[i + 1] + arr[i];
    }

    for (int slice = 0; slice < arr.size() - 1; slice++) {
      if (prefix[slice + 1] > postfix[slice + 1])
        ans++;
    }
    return ans;
  }
};
