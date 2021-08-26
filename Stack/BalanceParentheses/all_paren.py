from stack import Stack

def matches(top,symbol):
    open = "({["
    close = ")}]"
    return open.index(top) == close.index(symbol)

def paren_checker(paren):
    s = Stack()
    index = 0
    balanced = True

    while index <= len(paren) and balanced:
        symbol = paren[index]
        if symbol in "([{":
            s.push(symbol)
        elif s.is_empty():
            balanced = False
        else:
            top = s.pop()
            if not matches(top,symbol):
                balanced = False
        index +=1
    
    if s.is_empty() and balanced:
        return True
    else: 
        return False
    
print(paren_checker("({[]})"))
print(paren_checker("{]}()"))
            