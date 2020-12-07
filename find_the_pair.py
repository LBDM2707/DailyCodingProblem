# Given a list of numbers, return whether any two sums to k. 
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def find_pair(arr, k):
    dictionary = {}
    for x in arr:
        dictionary[x] = 1
        if (k-x) in dictionary:
            return (x, k -x)
        
    return "Not found"

def main():
    print("Problem 1")
    args = [10,15,3,7]
    print("Input array = {}".format(args))
    k = int(input("Enter K = "))
    print("Result = {}".format(find_pair(args,k)))

if __name__ == "__main__":
    main()