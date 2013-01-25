import re


def getcolor(value):
    '''Return color based on the color value in the resistor table'''
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
    return color[value]


def tolcolor(tol):
    '''Return Color for tolarance value'''
    val = int(tol * 100)
    if val == 100:
        return getcolor(1)
    if val == 200:
        return getcolor(2)
    if val == 50:
        return getcolor(5)
    if val == 25:
        return getcolor(6)
    if val == 10:
        return getcolor(7)
    if val == 5:
        return getcolor(8)
    if val == 500:
        return getcolor(-1)
    if val == 1000:
        return getcolor(-2)
    if val == 2000:
        return ""
    return -1


def valuetocolor(valuestr, tol=5, mul=None):
    digit = [0, 0, 0]
    dec = -1
    noofdigit = 0 if int(tol) > 2 else 1
    i = 0
    dot_mul_re = re.compile("^[0-9]*\.[0-9]+[kKmMrR]$")
    mul_re = re.compile("^[0-9]*[kKmMrR][0-9]+$")

    if dot_mul_re.match(valuestr):
        mul_char = valuestr[len(valuestr) - 1]
        valuestr = valuestr.replace(mul_char, '')
        valuestr = valuestr.replace('.', mul_char)

    if mul_re.match(valuestr):
        mul = None

    for x in valuestr.lstrip('0'):
        if x.isdigit():
            if i < 3:
                digit[i] = int(x)
            i += 1
        elif mul is None:
            if (x == 'r' or x == 'R' or x == '.'):
                mul = 0
            elif (x == 'k' or x == 'k'):
                mul = 3
            elif (x == 'm' or x == 'M'):
                mul = 6
            dec = i

    if dec == -1:
        dec = i
        if mul == None:
            mul = 0

    multiplier = mul + dec - noofdigit - 2
    multiplier = -2 if multiplier == -3 else multiplier

    if noofdigit == 0:
        ret = {"band1": getcolor(digit[0]),
                "band2": getcolor(digit[1]),
                "band3": getcolor(multiplier),
                "band4": "",
                "band5": tolcolor(tol)
                }
    else:
        ret = {"band1": getcolor(digit[0]),
                "band2": getcolor(digit[1]),
                "band3": getcolor(digit[2]),
                "band4": getcolor(multiplier),
                "band5": tolcolor(tol)
                }
    return ret
