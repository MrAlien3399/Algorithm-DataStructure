from stack import Stack

class Parenthesis:
    def __init__(self,paren):
        self.paren = paren # (())
    
    def check_balance(self):
        balanced = True
        index = 0
        s = Stack()

        while index < len(self.paren) and balanced:
            if self.paren[index] in "(":
                s.push(self.paren[index])
            elif s.is_empty():
                balanced = False
            else:
                s.pop()
            index += 1
        
        if s.is_empty() and balanced:
            return True
        else:
            return False

paren1 = Parenthesis("(())")
print(paren1.check_balance())
