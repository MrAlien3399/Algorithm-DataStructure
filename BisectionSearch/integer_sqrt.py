x = 9
low = 0.0
high = x
guess = (low+high)/2.0

while abs(guess**2 - x) >= 0.01:
    if guess ** 2 > x:
        high = guess
    else:
        low = guess
    guess = (low+high)/2.0

print(guess,"is close to the square root of",x)
