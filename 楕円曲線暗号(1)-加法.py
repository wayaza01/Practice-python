import math, time

start = time.time()
xp, yp, xq, yq = list(map(int, input().split()))
# y^2= x^3 + 3x + 4
a, b, p= 3, 7, 7

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
def plus(xp,yp,xq,yq,a,b,p):
    if xp==xq and yp!=yq:
        xr=-1
        yr=-1
    if xp==xq and yp==0 and yq==0:
        xr=-1
        yr=-1
    if xp==xq and yp+yq==p:
        xr=-1
        yr=-1
    else: 
        if xp==-1&yp==-1:
                xr=xq
                yr=yq
        elif xq==-1&yq==-1:
                xr=xp
                yr=yp
        elif yp==-yq:
                xr=-1
                yr=-1
        elif xp==xq:
            ramda=(((3*xp**2)+a)*findModInverse(2*yp,p))%p
            xr=(ramda**2-xp-xq)%p
            yr=(ramda*(xp-xr)-yp)%p
        else:
            if xp!=yp:
                xp,xq=xq,xp
                yp,yq=yq,yp
                ramda=((yp-yq)*findModInverse((xp-xq)%p,p))%p
                xr=(ramda**2-xp-xq)%p
                yr=(ramda*(xp-xr)-yp)%p
                xp,xq=xq,xp
                yp,yq=yq,yp
            
            else:
                ramda=((yp-yq)*findModInverse((xp-xq)%p,p))%p
                xr=(ramda**2-xp-xq)%p
                yr=(ramda*(xp-xr)-yp)%p
              
    return (xr,yr)
t = time.time() - start
T = round(t, 3)
print("time :", T)
