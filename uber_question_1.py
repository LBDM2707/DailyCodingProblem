# Use division

def generate_new_array(arr):
    big = 1
    for x in arr:
        big *= x
    return [int(big/x) for x in arr]

# Non-division version
def generate_new_array_v2(arr):
    
    return arr

def main():
    print("Problem 1")
    args = [1,2,3,4,5]
    print("Input array = {}".format(args))
    print("Result = {}".format(generate_new_array(args)))

if __name__ == "__main__":
    main()