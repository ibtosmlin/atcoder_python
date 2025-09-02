##############name##############
# 巡回セールスマン問題
######description######
# 巡回セールスマン問題
######body######
# bitDP
# dp[s][i]  集合sに行って、今iにいる場合の最小距離

INF = 10**9
n, m = map(int, input().split())

# 辺の情報
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    fm, to, d = map(int, input().split())
    # fm, to = fm - 1, to - 1
    dist[fm][to] = d

# 距離関数
def d(fm, to):
    if dist[fm][to] != INF:
        return dist[fm][to]
    else:
        # 何か変則処理
        # ex. dist[fm][to] = abs(a-p) + abs(b-q) + max(0, r-c)
        return dist[fm][to]

# dp[s][i]  集合sに行って、今iにいる場合の最小距離
# 最初は0だがsにはカウントしない
dp = [[INF] * n for _ in range(1 << n)]
for first in range(n):
    dp[1 << first][first] = d(0, first)

for s in range(1, 1 << n):
    for fm in range(n):
        if not s >> fm & 1: continue    # fmがsに無い場合->スキップ
        if dp[s][fm] == INF: continue   # 到達距離がINF->スキップ
        for to in range(n):
            if s >> to & 1: continue    # すでにtoがsにいる場合->スキップ
            next_s = s | (1 << to)      # toを追加した状態
            dp[next_s][to] = min(dp[next_s][to], dp[s][fm] + d(fm, to))

ret = dp[-1][0]

if ret == INF:
    print(-1)
else:
    print(ret)


######prefix######
# Lib_A_巡回セールスマン問題_TSP_bitDP
##############end##############
