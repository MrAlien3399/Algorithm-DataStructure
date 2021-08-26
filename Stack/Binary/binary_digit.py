from stack import Stack

def binary_digit(integer):
    s = Stack()
    while integer > 0:
        remainder = integer % 2
        s.push(remainder)
        integer //= 2
    
    binary_string = ""
    while not s.is_empty():
        binary_string += str(s.pop())
    
    return binary_string

print(binary_digit(23))