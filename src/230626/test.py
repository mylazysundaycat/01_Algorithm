def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a