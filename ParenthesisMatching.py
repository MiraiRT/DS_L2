s = input("Enter String : ")
l = []
opa = ['{', '[', '(']  # Opened Parenthesis
cpa = ['}', ']', ')']  # Closed Parenthesis
par = ['{}', '[]', '()']  # Correct Parenthesis
match = True
for i in s:
    if i in opa:
        l.append(i)
    if i in cpa:
        if len(l) == 0:
            print('Mismatched Parenthesis')
            match = False
            break
        elif str(l.pop() + i) in par:
            continue
        else:
            print('Mismatched Parenthesis')
            match = False
            break
if match and len(l) == 0:
    print('Correct Parenthesis')
