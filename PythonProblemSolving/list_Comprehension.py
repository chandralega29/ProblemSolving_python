# Problem: List Comprehensions

# Let's learn about list comprehensions!

# You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n.

# Print a list of all possible coordinates given by [i, j, k] on a 3D grid where:

# 0 ≤ i ≤ x
# 0 ≤ j ≤ y
# 0 ≤ k ≤ z

# The sum of the coordinates (i + j + k) must not be equal to n.

# Use list comprehensions rather than multiple loops.

# Example

# All permutations of [i, j, k] are generated using the ranges above.
# Print an array of those permutations where the sum of the coordinates is not equal to n.

# Input Format

# Four integers x, y, z and n, each on a separate line.

# Constraints

# 0 ≤ x, y, z ≤ 10
# 0 ≤ n ≤ 30

# Output Format

# Print the list in lexicographic increasing order.

# Sample Input 0
# 1
# 1
# 1
# 2

# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# Explanation 0

# Each variable i, j and k will have values of 0 or 1.

# All permutations of lists in the form [i, j, k] are:
# [0,0,0]
# [0,0,1]
# [0,1,0]
# [0,1,1]
# [1,0,0]
# [1,0,1]
# [1,1,0]
# [1,1,1]

# Remove all arrays that sum to 2 to leave only the valid permutations.

# Sample Input 1
# 2
# 2
# 2
# 2

# Sample Output 1
# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], 
#  [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], 
#  [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], 
#  [2, 2, 0], [2, 2, 1], [2, 2, 2]]


x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k]
          for i in range(x + 1)
          for j in range(y + 1)
          for k in range(z + 1)
          if i + j + k != n]

print(result)