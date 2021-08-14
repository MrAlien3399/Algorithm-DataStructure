x = 27
low = 0
high = x
guess = (low+high)/2.0

while abs(guess**3 - x) >= 0.01:
    if guess**3 > x:
        high = guess
    else:
        low = guess
    guess = (low+high)/2.0
    
print(guess,"is close to the cube root of",x)