from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ##set output list as li
        ##pop the first row of the matrix and append it into li as the same time

        ##append every single last number of a row to the li
        ##for each row in matrix
        ##pop last element in row and add to li
        ##check condition if matrix exist and matrix[0]
        ##add the remain element of the last row of list to li (reverse)
        ##for each row in reversed(matrix)
        ##pop the first number and add to li
        ##redo in while loop
        # O(n*m) time complexity and O(n*m) space complexity
        li = []
        while matrix:
            li += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    li.append(row.pop(-1))

            if matrix:
                li += matrix.pop(-1)[::-1]

            if matrix and matrix[0]:
                for row in reversed(matrix):
                    li.append(row.pop(0))
        return li
