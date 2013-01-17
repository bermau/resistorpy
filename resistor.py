def valuetocolor(valuestr, tol=0, mul=999):
    color = {-2: "silver",
            -1: "gold",
            0: "black",
            1: "brown",
            2: "red",
            3: "orange",
            4: "yellow",
            5: "green",
            6: "blue",
            7: "violet",
            8: "grey",
            9: "white"}
    digit = [0, 0, 0]
    dec = 0
    i = 0
    for x in valuestr:
        if x.isdigit():
            if i < 3:
                digit[i] = int(x)
            i += 1
        elif(mul == 999):
            if (x == 'r' or x == 'R' or x == '.'):
                mul = 0
                dec = i
            elif (x == 'k' or x == 'k'):
                mul = 3
                dec = i
            elif (x == 'm' or x == 'M'):
                mul = 6
                dec = i
    mul = i if mul == 999 else mul
    dec -= 2
    multiplier = mul + dec - tol
    multiplier = -2 if multiplier == -3 else multiplier
    if tol == 0:
        colors = [color[digit[0]], color[digit[1]], color[multiplier]]
    else:
        colors = [color[digit[0]], color[digit[1]], color[digit[2]],
        color[multiplier]]
    return colors


while True:
    valuestr = raw_input(">")
    print valuetocolor(valuestr, tol=0)
