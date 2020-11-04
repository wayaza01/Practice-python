import math, time

# 開始時間を格納する
start = time.time()
# P(xp, yp)と Q(xq, yq)の入力
xp, yp, xq, yq = list(map(int, input().split()))
# y^2= x^3 + 3x + 4
a = 3
p = 7

# http://inventwithpython.com/hacking (BSD Licensed)
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

# 加法公式
if (xp == 0 and yp == 0):
    xr = xq
    yr = yq
elif (xq == 0 and yq == 0):
    xr = xp
    yr = yp
else:
    if (yp == -yq):
        xr = 0
        yr = 0
    else:
        if (xp == xq):
            # X= (3*xp^2 + a)/(2*yp)
            X = ((3 * xp ** 2 + a) * findModInverse(2 * yp, p)) % p
            xr = (X * X - xp - xq) % p
            yr = (X * (xp - xr) - yp) % p
        else:
            # X= (yp-yq)/(xp-xq)
            X = ((yp - yq) * findModInverse((xp - xq) % p, p)) % p
            xr = (X * X - xp - xq) % p
            yr = (X * (xp - xr) - yp) % p

print("xr, yr: ", xr, ",", yr, )
print(X)

t = time.time() - start
T = round(t, 3)
# 現在時間から開始時間を引いた値(実行時間)を出力する
print("累積処理時間 :", T)