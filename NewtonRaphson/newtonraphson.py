x = 100
xp = x/2.0 #first guess

while abs(xp **2 - x) >= 0.01:
    xp = xp - (xp**2-x)/(2*xp)

print(xp)