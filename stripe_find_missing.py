# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer 
# that does not exist in the array. The array can contain duplicates and 
# negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] 
# should give 3.

# You can modify the input array in-place.

def find_missing_pos(arr):
    new_arr = {}
    for x in arr:
        new_arr[x] = x
    i = 1
    while (i in new_arr): 
        i += 1
    return i


def main():
    print("hello")
    result = find_missing_pos([1, 2, 0])
    print(result)
   

if __name__ == "__main__":
    main()