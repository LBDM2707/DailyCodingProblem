# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. The basic 
# idea is to represent repeated successive characters as a single count and 
# character. For example, the string "AAAABBBCCDAA" would be encoded as 
# "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be 
# encoded have no digits and consists solely of alphabetic characters. You can 
# assume the string to be decoded is valid.

def encode(s):
    result=""
    count = 0
    ch = None
    for c in s:
        if ch == c:
            count += 1
        else:
            if ch != None:
                result += str(count) +  ch
            ch = c
            count = 1
    return result

def decode(s):
    result = ""
    tmp = ""
    for ch in s:
        if (""+ch).isnumeric():
            tmp += ch
        else:
            count = int(tmp)
            tmp = ""
            for i in range(count):
                result+=ch

    return result




print(encode("AAAABBBCCDAA"))
print(decode("4A3B2C1D"))