# def validateBrackets(string):
#     length = len(string)

opening_brackets = ["[","{","("]
closing_brackets = ["]","}",")"]

def validateBrackets(brackets_string):
    brackets_list = []
    for i in brackets_string:
        if i in opening_brackets:
            brackets_list.append(i)
        elif i in closing_brackets:
            pos = closing_brackets.index(i)
            if ((len(brackets_list) > 0) and
                (opening_brackets[pos] == brackets_list[len(brackets_list)-1])):
                brackets_list.pop()
            else:
                return False
    if len(brackets_list) == 0:
        return True
    else:
        return False


# Driver code
string = "{[]{()}}"
if validateBrackets(string):
    print(string, ' isBalanced')
else:
    print(string, 'is not Unbalanced')

string = "[{}{})(]"
if validateBrackets(string):
    print(string, ' isBalanced')
else:
    print(string, 'is not Unbalanced')

string = "((()"
if validateBrackets(string):
    print(string, ' isBalanced')
else:
    print(string, 'is not Unbalanced')
