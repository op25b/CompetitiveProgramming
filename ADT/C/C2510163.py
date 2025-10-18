# ADT2510163C
# https://atcoder.jp/contests/adt_medium_20251016_3/tasks/abc352_b

S_STR = input()
T_STR = input()

s_index = 0
answer = []
for t_index in range(len(T_STR)):
  if S_STR[s_index] == T_STR[t_index]:
    answer.append(t_index + 1)
    s_index += 1
  t_index += 1

print(*answer)