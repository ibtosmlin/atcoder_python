#name#
# reverse=True
#description#
# ソートでのリバース
#body#
reverse=True
#prefix#
# reverse=True
#end#

#name#
# sort(key=itemgetter
#description#
# itemgetterソート
#body#
sort(key=lambda x: x[1])
#prefix#
# sort(key=l
#end#

#name#
# 順列・組み合わせ
#description#
# 順列・組み合わせ
#body#
from itertools import *
P = list(permutations(range($n), r))   # 順列(nPr)
C = list(combinations(range($n), r))   # 組み合わせ(nCr)
CR = list(combinations_with_replacement(range($n), r))  # 重複も許容した組み合わせ(nHr=n+r-1Cr)
PN = list(product(range($n), repeat=r)) # 重複順列(n**r)
T = [[1, 2],[3, 4, 5, 6],[7, 8, 9]]
PT = list(product(*T))

from more_itertools import distinct_combinations, distinct_permutations

#prefix#
# itertools
# Lib_順列・組み合わせ
#end#

#name#
# direc
#description#
# direc
#body#
direc = {"U":(0, 1), "R":(1, 0), "D":(0, -1), "L":(-1, 0)}
direc = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def isin(i, j, H, W): return ~((0 <= i < H) and (0 <= j < W))
def isnotin(i, j, H, W): return not isin(i, j, H, W)

for di, dj in direc:
    ni = i + di
    nj = j + dj

#prefix#
# direc_canmove
#end#
