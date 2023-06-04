# Goal: reverse the content of an array

def reverseArray(a):
    i = len(a)-1
    reverse_array = []
    while i >= 0:
        reverse_array.append(a[i])
        i -= 1
    return reverse_array



