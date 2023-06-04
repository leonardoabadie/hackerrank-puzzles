# Given any array x, say [1, 5, 10, 7, -2], create an algorithm that shifts each
# number by one to the front. For example, when the program is done, the array
# [1, 5, 10, 7, -2] should become [5, 10, 7, -2, 0].

def shift_values_array(arr):
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[len(arr)-1] = 0
    return arr
