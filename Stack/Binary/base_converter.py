from stack import Stack

def base_converter(integer,base):
    digits = "0123456789ABCDEF"
    s = Stack()
    while integer > 0:
        remainder = integer % base
        s.push(remainder)
        integer //= base

    new_string = "" 
    while not s.is_empty():
        new_string += digits[s.pop()]
    
    return new_string

print(base_converter(250,16))

