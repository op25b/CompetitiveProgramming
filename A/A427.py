s_str = input()
s_len = len(s_str)

center = (s_len * 1) // 2

answer = s_str[0: center] + s_str[center + 1 : s_len]

print(answer)