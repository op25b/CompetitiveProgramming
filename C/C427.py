# ABC427C
# https://atcoder.jp/contests/abc427/tasks/abc427_c

NODE_INT, BRANCH_INT = map(int, input().split())
BRANCH_LIST = [list(map(int, input().split())) for _ in range(BRANCH_INT)]

min_cut_int = BRANCH_INT
for combination_int in range(2**(NODE_INT - 1)):
  WHITE_NODE_LIST = [1]
  BLACK_NODE_LIST = []

  # 頂点2以降の色を２進数で表現する
  COMBINATION_BIN_STR = format(combination_int, '0' + str(NODE_INT - 1) + 'b')
  for digit in range(len(COMBINATION_BIN_STR)):
    if COMBINATION_BIN_STR[digit] == '1':
      # 頂点0が存在せず、頂点1は白に固定しているため、頂点2以降は（digit + 2）で表される
      WHITE_NODE_LIST.append(digit + 2)
    else:
      BLACK_NODE_LIST.append(digit + 2)

  cut_int = 0
  for branch in BRANCH_LIST:
    if (branch[0] in WHITE_NODE_LIST and branch[1] in WHITE_NODE_LIST) or \
       (branch[0] in BLACK_NODE_LIST and branch[1] in BLACK_NODE_LIST):
      cut_int += 1

  if cut_int < min_cut_int:
    min_cut_int = cut_int

print(min_cut_int)