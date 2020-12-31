# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return 
# whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.

def check_brackets(s):
    queue = []
    while len(s) > 0:
        ch = s[0]
        s = s[1:]
        if ch in ["{", "(", "["]:
            queue.insert(0, ch)
        else:
            if len(queue) == 0:
                return False
            ch2 = queue.pop(0)
            if ch == "]" and ch2 != "[":
                return False
            if ch == "}" and ch2 != "{":
                return False    
            if ch == ")" and ch2 != "(":
                return False
    return True if len(queue) == 0 else False


print(' Need True = {}'.format(check_brackets("([])[]({})")))
print(' Need False = {}'.format(check_brackets("([)]")))
print(' Need False = {}'.format(check_brackets("((()")))