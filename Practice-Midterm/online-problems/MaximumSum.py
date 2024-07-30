# Problem no.1146
# Website: https://acm.timus.ru/problem.aspx?space=1&num=1146

def kadane_2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    #start from left column 0-3, 1-3, 2-3 to 
    # find group of number that has maximum sum
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

        # [[0 -2 -7 0], 
        #   [9 2 -6 2],   
        #   [-4 1 -4 1],  
        #   [-1 8 0 -2]]

        #Transform to this (it sum column to another column then compute)

        #column 0 to 3
        #loop 0 [0, 9, -4, -1]
        #loop 1 [0 + (-2), 9 + 2, -4 + 1, -1 + 8] -> [-2, 11, -3, 7]
        #loop 2 [-9, 5, -7, 7]
        #loop 3 [-9, 7, -6, 5]

        # Find the maximum sum of the temporary array using a direct approach
            max_current = max_global = temp[0]
            for num in temp[1:]:
                max_current = max(num, max_current + num)
                if max_current > max_global:
                    max_global = max_current

            max_sum = max(max_sum, max_global)

    return max_sum

n = int(input())
list_numbers = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    list_numbers.append(numbers)

print(kadane_2d(list_numbers))