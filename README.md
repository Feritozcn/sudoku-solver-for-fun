##Sudoku Solver for Fun
Key Details:
Worst-case Time Complexity:
𝑂
(
9
𝑛
)
O(9 
n
 )

𝑛
n: The number of empty cells on the Sudoku board.
This represents the maximum number of states the algorithm may explore in the worst-case scenario (all cells are empty).
Space Complexity:
𝑂
(
𝑛
)
O(n)

Space is used primarily for the recursion stack. The maximum depth of recursion equals the number of empty cells.
Usage Notes:
Input Requirements:

The board should be a 9x9 grid of strings.
Use "." to represent empty cells.
All numbers on the board should be strings (e.g., "1", "2", etc.).
Additional Considerations:

Ensure proper validation of input data.
This implementation is for fun and may not be optimized for large-scale or competitive use.
