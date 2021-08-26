from stack import Stack

def rev_str(string):
    s = Stack()
    index = 0
    while index < len(string):
        s.push(string[index])
        index += 1
    
    reverse_string  = ""
    while not s.is_empty():
        reverse_string += s.pop()
    
    return reverse_string

print(rev_str("Hello World"))