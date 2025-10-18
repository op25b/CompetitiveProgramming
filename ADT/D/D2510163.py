# ADR2510163D
# https://atcoder.jp/contests/adt_medium_20251016_3/tasks/abc303_b

N_INT, M_INT = map(int, input().split())
A_LIST = [list(map(int, input().split())) for _ in range(M_INT)]

# 全ての２人の組み合わせをキーにもつディクショナリを作成
combination_dict = {}
for person1 in range(N_INT):
  for person2 in range(person1 + 1, N_INT):
    PAIR_SET = frozenset([person1 + 1, person2 + 1]) # 人の番号は１から始まるから+1
    combination_dict[PAIR_SET] = False

# 隣り合う人の組み合わせが存在すればTrueに更新
for line in A_LIST:
  for person_index in range(len(line) - 1):
    PAIR_SET = frozenset([line[person_index], line[person_index + 1]])
    combination_dict[PAIR_SET] = True

ANSWER = sum(1 for v in combination_dict.values() if v == False)
print(ANSWER)