#title#
# 順列のライブラリ
#subtitle#
# permutationクラス:
# id_of_permutation(): 何番目か
# kth_permutation(k): k番目を出力
# prev():前の順列
# next():次の順列

#name#
# Lib_permutation
#description#
# 順列のライブラリ
#body#

class permutation:
    def __init__(self, L):
        self.n = len(L)
        self.L = L
        self.LS = sorted(L[:])
        self.map = {li: i for i, li in enumerate(self.LS)}
        nn = self.n + 1
        fa = [1] * (nn + 1)
        for i in range(nn):
            fa[i+1] = fa[i] * (i+1)
        self.fa = fa
        self.convL = self._convL(self.L)
        self.facn = self.fa[self.n]
        self.k = self.id_of_permutation(self.L)

    def _convL(self, L):
        return [self.map[li] for li in L]

    def _restoreP(self, P):
        return [self.LS[i] for i in P]

    def _kth_permutation(self, k):
        # zero-indexed here
        n = self.n
        S = [i for i in range(n)]
        L = []
        for i in range(n):
            a = self.fa[n-1-i]
            j = k // a
            k %= a
            L.append(S[j])
            S = S[:j] + S[j+1:]
        return L

    def _id_of_permutation(self, P):
        # zero-indexed here
        ret = 0
        while len(P) > 1:
            a = len([l for l in P if l < P[0]])
            ret += a * self.fa[len(P) - 1]
            P = P[1:]
        return ret

    def id_of_permutation(self, L=None)->int:
        """
        return: 順列の辞書順
        """
        if L:
            P = self._convL(L)
            return self._id_of_permutation(P)
        else: return self.k

    def kth_permutation(self, k)->list:
        """
        return: k番目の順列
        """
        P = self._kth_permutation(k)
        return self._restoreP(P)

    def prev(self, L=None):
        """
        return: 初期順列または入力順列のひとつ前
        """
        if L:
            k = self.id_of_permutation(L)
        else:
            k = self.k
        if k == 0: return None
        return self.kth_permutation(self.k - 1)

    def next(self, L=None):
        if L:
            k = self.id_of_permutation(L)
        else:
            k = self.k
        if k + 1 == self.facn: return None
        return self.kth_permutation(k + 1)

##################################
N = int(input())
P = [int(a) for a in input().split()]
mut = permutation(P)
print(*mut.prev())

#prefix#
# Lib_permutation_順列
#end#
