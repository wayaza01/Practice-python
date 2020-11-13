import math, time

start = time.time()
# P(xp, yp)
xp, yp = map(int, input().split())
# スカラーk(10進数)
k = int(input()) 
# y^2 = x^3 + ax + b 
p= 7
# Q<-P
xq, yq= xp, yp
# 10進数->2進数
k_2= format(k, 'b')

l= list(k_2)
print(l)
#################################################################
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
#################################################################
a= 6
c= 1 

for c in range(len(k_2)): 
    if l[c]== '0':
        if(xq==0 and yq==0):
            xq= xq
            yq= yq
        else:
            X= ((3*xq**2 + a)*findModInverse(2*yq, p))%p
            xq= (X*X-xq-xq)%p
            yq= (X*(xq-xq)-yq)%p
                
    elif l[c]== '1':
        if(xq==0 and yq==0):
            xq= xq
            yq= yq
            ### 2Q + P ###
            if(xp==0 and yp==0):
                xq= xq
                yq= yq
            elif(xq==0 and yq==0):
                xq= xp
                yq= yp
            else:
                if(yp==-yq):
                    xq= 0
                    yq= 0
                else:
                    if(xp==xq):
                        X= ((3*xp**2 + a)*findModInverse(2*yp, p))%p
                        xq= (X*X-xp-xq)%p
                        yq= (X*(xp-xq)-yp)%p
                    else:
                        X= ((yp-yq)*findModInverse((xp-xq)%p,p))%p
                        xq= (X*X-xp-xq)%p
                        yq= (X*(xp-xq)-yp)%p
            
        else:
            X= ((3*xq**2 + a)*findModInverse(2*yq, p))%p
            xq= (X*X-xq-xq)%p
            yq= (X*(xq-xq)-yq)%p
            ### 2Q + P ###
            if(xp==0 and yp==0):
                xq= xq
                yq= yq
            elif(xq==0 and yq==0):
                xq= xp
                yq= yp
            else:
                if(yp==-yq):
                    xq= 0
                    yq= 0
                else:
                    if(xp==xq):
                        X= ((3*xp**2 + a)*findModInverse(2*yp, p))%p
                        xq= (X*X-xp-xq)%p
                        yq= (X*(xp-xq)-yp)%p
                    else:
                        X= ((yp-yq)*findModInverse((xp-xq)%p,p))%p
                        xq= (X*X-xp-xq)%p
                        yq= (X*(xp-xq)-yp)%p
                    
    print(c+2, "倍 :", xq, yq)

t = time.time() - start 
T = round(t, 3)
#現在時間から開始時間を引いた値(実行時間)を出力する
print("累積処理時間 :", T)
