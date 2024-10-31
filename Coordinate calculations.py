import math


def jsx(x1, y1, x2, y2):  # 坐标增量计算Coordinate increment calculation
    dax = x2 - x1
    day = y2 - y1
    return math.fabs((day) / (dax))


# azimuth
def fwj(x1, y1, x2, y2):
    if (x2 - x1) > 0 and (y2 - y1) > 0:
        c = jsx(x1, y1, x2, y2)
        e = (math.atan(c) * ((180) / (math.pi)))
        return e
    if (x2 - x1) < 0 and (y2 - y1) > 0:
        c2 = jsx(x1, y1, x2, y2)
        e2 = 180 - (math.atan(c2) * ((180) / (math.pi)))
        return e2
    if (x2 - x1) < 0 and (y2 - y1) < 0:
        c3 = jsx(x1, y1, x2, y2)
        e3 = (math.atan(c3) * ((180) / (math.pi))) + 180
        return e3
    if (x2 - x1) > 0 and (y2 - y1) < 0:
        c4 = jsx(x1, y1, x2, y2)
        e4 = 360 - (math.atan(c4) * ((180) / (math.pi)))
        return e4


# distance
def jl(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    return d


# dfm
def dfm(f):
    d = math.floor(f)
    f1 = math.floor((f - d) * 60)
    m = math.floor((((f - d) * 60) - f1) * 60)
    dfm1 = d + f1 / 100 + m / 10000
    return dfm1

