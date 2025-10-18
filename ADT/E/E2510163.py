# ADT2510163E
# https://atcoder.jp/contests/adt_medium_20251016_3/tasks/abc227_c

# ギブアップ

import math

N_INT = int(input())

answer = 0
# 条件より、aの最大値はNの立方根
for a in range(1, math.floor(N_INT ** (1 / 3)) + 1):
  # 条件より、bの最大値は(N/a)の平方根
  for b in range(a, math.floor((N_INT / a) ** (1 / 2)) + 1):
    # aとbを定めれば、条件を満たすcの個数は計算できる
    answer += N_INT // (a * b) - b + 1

print(answer)
