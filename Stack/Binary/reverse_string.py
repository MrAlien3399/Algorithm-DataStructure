from stack import Stack

s = Stack()

def reverse_str(string):
    for i in string:
        s.push(i)
    
    r_string = ""
    for v in range(len(string)):
        r_string += s.pop()

    print(r_string)

s = reverse_str("hello")