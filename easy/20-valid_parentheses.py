# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false

def lint_the_strings(s):
    result = True
    sn2 = s
    print(type(s), type(sn2))
    for index, letter in enumerate(s):
        search_correspondance = False
        result = False
        if any(letter == x for x in [")", "]", "}"]):
            return result
        if letter == "(":
            for letter2 in s[index:]:
                if letter2 == ")":
                    result = True
                    break
                elif any(letter2 == x for x in  ["]", "}"]):
                   break
        if letter == "{":
            for letter2 in s[index:]:
                if letter2 == "}":
                    result = True
                    break
                elif any(letter2 == x for x in ["]", ")"]):
                    break
        if letter == "[":
            for letter2 in s[index:]:
                if letter2 == "]":
                    result = True
                    break
                elif any(letter2 == x for x in [")", "}"]):
                    break
    return result

def valid_parenthesis(s):
    # create a list to use it as a stack

    stack = []
    existing_possibilities = {"()", "[]", "{}"}
    result = True
    if len(s) < 2 or not any(letter in s for letter in ")]}"):
        return False
    for index, letter in enumerate(s):
        if letter in "([{" and index < len(s)-1:
            stack.append(letter)
            print(f'1 | index: {index}, stack: {stack}, letter: {letter}')
            continue
#        if stack == [] and letter in ")]}":
#            result = False
        elif stack != [] and f'{stack.pop()}{letter}' in existing_possibilities:
            print(f'2 | index: {index}, stack: {stack}, letter: {letter}')
            result = result and True
        else:
            return False
    return result


s0 = ""
s1 = "("
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "()"
s6 = ")"
s7 = "]"
s8 = "}"
s9 = "(){}}{"
s10 = "[]"
s11 = "{}"
s12 = "((" 
s13 = "{[]}"
s14 = "([]){"
s15 = "([]"






#print(valid_parenthesis(s9))
#print(valid_parenthesis(s2))


#valid_parenthesis(s2)
#    assert valid_parenthesis(s5) == True
#    assert valid_parenthesis(s10) == True
#    assert valid_parenthesis(s11) == True

import sys
import traceback

print(valid_parenthesis(s13))

cond = True

if cond:
    try:
        assert valid_parenthesis(s0) == False
        assert valid_parenthesis(s1) == False
        assert valid_parenthesis(s2) == True
        assert valid_parenthesis(s3) == False
        assert valid_parenthesis(s4) == False
        assert valid_parenthesis(s5) == True
        assert valid_parenthesis(s6) == False
        assert valid_parenthesis(s7) == False
        assert valid_parenthesis(s8) == False
        assert valid_parenthesis(s9) == False
        assert valid_parenthesis(s10) == True
        assert valid_parenthesis(s11) == True
        assert valid_parenthesis(s12) == False
        assert valid_parenthesis(s13) == True
        assert valid_parenthesis(s14) == False
        assert valid_parenthesis(s15) == False
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))


#assert lint_the_strings(s0) == True
#assert lint_the_strings(s1) == False
#assert lint_the_strings(s2) == True
#assert lint_the_strings(s3) == False
#assert lint_the_strings(s4) == False
#assert lint_the_strings(s5) == True
#assert lint_the_strings(s6) == False
#assert lint_the_strings(s7) == False
#assert lint_the_strings(s8) == False



var1 = True
var1 = var1 and True
var1 = var1 and True

#print(var1)