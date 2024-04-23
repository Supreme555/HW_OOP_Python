def is_balanced(s):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            # возвращает словари
            if not stack or brackets[stack.pop()] != char:
                return "no"
    
    return "yes" if not stack else "no"

sequence = input()

print(is_balanced(sequence))
