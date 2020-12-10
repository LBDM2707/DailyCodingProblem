# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the 
# number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa',
# 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not 
# allowed.

# Sound like a case for dynamic progamming. Very simialar to the "return the changes"

# Try recursive
def decodes_count_v1(s):
    if len(s) < 2:
        return 1
    else:
        single = decodes_count_v1(s[1:])
        double = decodes_count_v1(s[2:]) if int(s[:2]) <= 26 else 0
        return single + double


def main():
    print("Hello, this problem is by Facebook 10/20/2020")
    s = input("Enter string: ")
    print("RESULT = {}".format(decodes_count_v1(s)))


if __name__ == "__main__":
    main()
