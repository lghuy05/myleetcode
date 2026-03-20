class Solution {
public:
  bool isValidSudoku(vector<vector<char>> &board) {
    vector<unordered_set<char>> rows_arr(9);
    vector<unordered_set<char>> cols_arr(9);
    vector<unordered_set<char>> box_arr(9);
    int rows = board.size();
    int cols = board[0].size();
    // rows
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (board[i][j] == '.') {
          continue;
        }
        if (rows_arr[i].count(board[i][j])) {
          return false;
        }
        rows_arr[i].insert(board[i][j]);
      }
    }
    // cols
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (board[j][i] == '.') {
          continue;
        }
        if (cols_arr[i].count(board[j][i])) {
          return false;
        }
        cols_arr[i].insert(board[j][i]);
      }
    }
    // box

    //(0,0), (0,1), (0,2), (1,0), (1,1),(1,2), (2,0),(2,1),(2,2)
    int box;
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        box = (j / 3) + (i / 3) * 3;
        if (board[i][j] == '.') {
          continue;
        }
        if (box_arr[box].count(board[i][j])) {
          return false;
        }
        box_arr[box].insert(board[i][j]);
      }
    }
    return true;
  }
};
