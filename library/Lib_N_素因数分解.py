#title#
# 素因数分解

#subtitle#
# prime_factorize(n) -> {prime: degree}
# prime_factorize(A) 複数個版

#name#
# 素因数分解prime_factorize
#descripiton#
# 素因数分解
#body#
##############################
# 素因数分解
# nは10**15くらいまでOK
# returns dict s.t. key = {prime}   value = {degree}
##############################
def prime_factorize(n:int) -> dict:
    if n == 1: return {1: 1}
    pd = dict()
    test = [2] + list(range(3, int(n**0.5)+1, 2))
    for p in test:
        if n % p != 0: continue
        d = 0
        while n % p == 0:
            d += 1
            n //= p
        pd[p] = d
    if n != 1: pd[n] = 1
    return pd

print(prime_factorize(360))
# 72 = 2**3 * 3**2 * 5**1
# {2: 3, 3: 2, 5: 1}

##############################
# 素因数分解（複数個版）
# max(A)が大きい場合はNG  10**6くらいまで
# 最初に素数一覧を作っておく
##############################
def prime_factorize(A : list):
    Max = max(A) + 1
    IsPrime = [True] * Max
    MinFactor = [-1] * Max
    dica = {}
    IsPrime[0], IsPrime[1] = False, False
    MinFactor[0], MinFactor[1] = 0, 1
    for p in range(2, Max):
        if IsPrime[p]:
            MinFactor[p] = p
            for k in range(p*2, Max, p):
                IsPrime[k] = False
                if MinFactor[k] == -1:
                    MinFactor[k] = p

    ret = []
    for a in A:
        res = dict()
        while a != 1:
            prime = MinFactor[a]
            exp = 0
            while MinFactor[a] == prime:
                exp += 1
                a //= prime
            res[prime] = exp
            if not prime in dica:
                dica[prime] = 1
            else:
                dica[prime] += 1
        ret.append(res)
    return ret

##############################
# n!が素数pで何回割れるか O(logn)
# legendre(n, p)
##############################
def legendre(n, p):
    ret = 0
    while n > 0:
        ret += n // p
        n //= p
    return ret

#prefix#
# Lib_N_素因数分解
#end#
