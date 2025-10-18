# ABC427B
# https://atcoder.jp/contests/abc427/tasks/abc427_b

N_INT = int(input())

total = 0

for n_int_i in range(N_INT):
  if n_int_i == 0:
    total = 1
    continue
  
  TOTAL_STR = str(total)
  for total_char in TOTAL_STR:
    total += int(total_char)

print(total)