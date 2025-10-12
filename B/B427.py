n_int = int(input())

total = 0

for n_int_i in range(n_int):
  if n_int_i == 0:
    total = 1
    continue
  
  total_str = str(total)
  for total_char in total_str:
    total += int(total_char)

print(total)