# ABC427A
# https://atcoder.jp/contests/abc427/tasks/abc427_a

S_STR = input()
S_LEN = len(S_STR)

CENTER = (S_LEN * 1) // 2

ANSWER = S_STR[0: CENTER] + S_STR[CENTER + 1 : S_LEN]

print(ANSWER)