# This problem was asked by Google.

# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory
# subdir2 containing a file file.ext.

# The string 
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 
# represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext

# The directory dir contains two sub-directories subdir1 and subdir2. subdir1
# contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
# subdir2 contains a second-level sub-directory subsubdir2 containing a file 
# file2.ext.

# We are interested in finding the longest (number of characters) absolute path
# to a file within our file system. For example, in the second example above, 
# the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length
# is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the 
# length of the longest absolute path to a file in the abstracted file system. 
# If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.


# Check file name regex
import re
def is_file(file_name):
    file_pattern = "^[a-z0-9A-Z]+\.[a-z0-9A-Z]+$"
    return bool(re.match(file_pattern, file_name))

def get_longest_path(s):
    prep_data = s.split("\n")
    max = 0
    memory = []
    curr_level = -1
    for item in prep_data:
        # get level & value
        level = 0
        while len(item) > 1 and item[:1] == "\t":
            item = item[1:]
            level += 1 
        value = len(item) + (1 if level > 0 else 0)
        is_filename = is_file(item)
        # assess node
        if level > curr_level:
            curr_level = level
            memory.append(value)  
        else: # level is less than or equal curr level            
            curr_level = level
            memory[curr_level] = value
        
        # check if for path length
        if is_filename:
            temp = sum([memory[x] for x in range(0, curr_level)]) + value
            max = temp if temp > max else max
    return max
    

    
test_string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(get_longest_path(test_string))




